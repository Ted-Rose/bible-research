from django.contrib.auth import get_user_model
from rest_framework import serializers
from bible.models import Verse
from bible.serializers import VerseSerializer
from .models import Note, NoteVerse, Tag
User = get_user_model()


class CurrentAuthenticatedUserDefault:
    """Custom default callable for authenticated user field.
    Returns the current user if authenticated, otherwise the guest user.
    """
    requires_context = True

    def __call__(self, serializer_field):
        request = serializer_field.context.get('request')
        if (request and hasattr(request, 'user') and
                request.user.is_authenticated):
            return request.user
        # Return guest user instead of None
        try:
            return User.objects.get(username='guest')
        except User.DoesNotExist:
            # If guest user doesn't exist, return None
            # The create method will handle this case
            return None


class TagSerializer(serializers.ModelSerializer):
    """Serializes Tag model data for API input and output.
    Includes the 'parent_tag' as its primary key for relationships.
    """
    parent_tag = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        allow_null=True,
        required=False,
        default=None
    )
    user = serializers.HiddenField(
        default=CurrentAuthenticatedUserDefault()
    )
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Tag
        fields = [
            'id', 'user', 'name', 'parent_tag',
            'created_at', 'updated_at',
        ]
        # 'read_only_fields' makes sure 'id', 'created_at', 'updated_at' are
        # automatically handled by Django and not expected in user input.
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'parent_tag': {'default': None}
        }

    def create(self, validated_data):
        # If user is None, try to use guest user
        if 'user' in validated_data and validated_data['user'] is None:
            try:
                validated_data['user'] = User.objects.get(username='guest')
            except User.DoesNotExist:
                # If guest user doesn't exist, remove user field
                # to let the model use its default
                validated_data.pop('user')
        return super().create(validated_data)


class NoteVerseReferenceSerializer(serializers.Serializer):
    """Serializer to accept verse details for linking to a Note.
    This is for WRITE operations (e.g., when creating a Note).
    """
    book = serializers.CharField(
        max_length=50,
        help_text="The book name (e.g., 'John')."
    )
    chapter = serializers.IntegerField(
        help_text="The chapter number (e.g., 3)."
    )
    verse = serializers.IntegerField(
        help_text="The verse number (e.g., 16)."
    )


class NoteSerializer(serializers.ModelSerializer):
    """Serializes Note model data.
    - For POST/PUT: Accepts tag UUID and a list of verse
      references (book, chapter, verse).
    - For GET: Displays full tag object and full verse objects.
    """
    tag = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        allow_null=True,
        required=False,
        help_text="UUID of the primary Tag associated with this note."
    )
    user = serializers.HiddenField(
        default=CurrentAuthenticatedUserDefault()
    )
    verse_references = NoteVerseReferenceSerializer(
        many=True,
        write_only=True,
        required=False,
        help_text=(
            "List of objects, each with 'book', 'chapter', and 'verse' "
            "to link to the note."
        )
    )

    class Meta:
        model = Note
        fields = [
            'id', 'user', 'note_text', 'created_at', 'updated_at',
            'tag', 'verse_references'
        ]

    def create(self, validated_data):
        """
        Overrides the default create method to handle nested verse_references.
        """
        # Pop out the 'verse_references' as it's not a direct field on the Note
        verse_references_data = validated_data.pop('verse_references', [])
        # If user is None, try to use guest user
        if 'user' in validated_data and validated_data['user'] is None:
            try:
                validated_data['user'] = User.objects.get(username='guest')
            except User.DoesNotExist:
                # If guest user doesn't exist, remove user field
                validated_data.pop('user')
        # Create the Note instance using the remaining validated data
        note = Note.objects.create(**validated_data)

        # Handle the many-to-many relationship with verses via NoteVerse
        if verse_references_data:
            note_verse_instances = []
            for verse_ref_data in verse_references_data:
                try:
                    # Attempt to retrieve the Verse instance using
                    # case-insensitive book match
                    verse_instance = Verse.objects.get(
                        book__iexact=verse_ref_data['book'],
                        chapter=verse_ref_data['chapter'],
                        verse=verse_ref_data['verse']
                    )
                    # Create a NoteVerse instance to link the note and verse
                    note_verse_instances.append(
                        NoteVerse(note=note, verse=verse_instance)
                    )
                except Verse.DoesNotExist:
                    error_msg = (
                        f"Verse not found for '{verse_ref_data['book']} "
                        f"{verse_ref_data['chapter']}:"
                        f"{verse_ref_data['verse']}'. "
                        f"Please ensure the verse exists in your database."
                    )
                    raise serializers.ValidationError(error_msg)
                except Exception as e:
                    raise serializers.ValidationError(
                        f"Error processing verse reference: {e}"
                    )

            # Bulk create the intermediary NoteVerse instances for efficiency
            NoteVerse.objects.bulk_create(note_verse_instances)

        return note

    def to_representation(self, instance):
        """
        Overrides the default representation for GET requests to include
        nested tag and verse data instead of just their IDs.
        """
        # Get the default representation
        representation = super().to_representation(instance)
        # Include full verse objects instead of just IDs
        verses = instance.verses.all()
        representation['verses'] = VerseSerializer(verses, many=True).data
        # Include full tag object if a tag exists
        if instance.tag:
            representation['tag'] = TagSerializer(instance.tag).data
        return representation
