import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from annotations.serializers import TagSerializer, NoteSerializer
from bible.models import Verse


class SerializerTestCase(TestCase):
    """Test case for Tag and Note serializers with an authenticated user."""

    def setUp(self):
        """Set up test data and authentication."""
        # Create a test user
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )

        # Create a factory for requests
        factory = APIRequestFactory()
        request = factory.get('/')
        # Force authentication
        request.user = self.user
        # Create a proper request context
        self.context = {'request': Request(request)}

        # Create test verse
        self.verse, _ = Verse.objects.get_or_create(
            book='John',
            chapter=3,
            verse=16
        )

    def test_tag_serializer(self):
        """Test that TagSerializer correctly creates a tag."""
        # Use timestamp to ensure unique tag name
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        tag_data = {'name': f'AuthTag_{timestamp}'}
        
        # Create and validate serializer
        tag_serializer = TagSerializer(data=tag_data, context=self.context)
        self.assertTrue(tag_serializer.is_valid(), f"Tag validation errors: {tag_serializer.errors}")
        
        # Save and verify tag
        tag = tag_serializer.save()
        self.assertIsNotNone(tag.id)
        self.assertEqual(tag.name, tag_data['name'])
        
        return tag  # Return for use in other tests

    def test_note_serializer(self):
        """Test that NoteSerializer correctly creates a note with verse references."""
        # First create a tag to associate with the note
        tag = self.test_tag_serializer()
        
        # Prepare note data
        note_data = {
            'note_text': 'This is a test note with authenticated user',
            'tag': tag.id,
            'verse_references': [
                {'book': 'John', 'chapter': 3, 'verse': 16}
            ]
        }
        
        # Create and validate serializer
        note_serializer = NoteSerializer(data=note_data, context=self.context)
        self.assertTrue(note_serializer.is_valid(), f"Note validation errors: {note_serializer.errors}")
        
        # Save and verify note
        note = note_serializer.save()
        self.assertIsNotNone(note.id)
        self.assertEqual(note.note_text, note_data['note_text'])
        self.assertEqual(note.tag.id, tag.id)
        
        # Verify verse references
        self.assertEqual(note.verses.count(), 1)
        verse = note.verses.first()
        self.assertEqual(verse.book, 'John')
        self.assertEqual(verse.chapter, 3)
        self.assertEqual(verse.verse, 16)
