# Django imports
from django.db.models import Count

# Third-party imports
from rest_framework import serializers

# Local imports - external apps
from bible.models import Verse
from bible.serializers import VerseSerializer

# Local imports - current app
from .models import Note, NoteVerse, Tag

class TagSerializer(serializers.ModelSerializer):
    """
    Serializes Tag model data for API input and output.
    Includes the 'parent_tag' as its primary key for relationships.
    """
    parent_tag = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Tag
        fields = [
            'id',
            # 'user',
            'name',
            'parent_tag',
            'created_at',
            'updated_at',
        ]
        # 'read_only_fields' makes sure 'id', 'created_at', 'updated_at' are
        # automatically handled by Django and not expected in user input.
        read_only_fields = ['id', 'created_at', 'updated_at']


class NoteVerseReferenceSerializer(serializers.Serializer):
    """
    Serializer to accept verse details for linking to a Note.
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
    """
    Serializes Note model data.
    - For POST/PUT: Accepts tag UUID and a list of verse
      references (book, chapter, verse).
    - For GET: Displays full tag object and full verse objects.
    """
    # Accept UUID for tag, automatically maps to Tag instance
    tag = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        allow_null=True,
        required=False,
        help_text="UUID of the primary Tag associated with this note (optional)."
    )

    # This field is write-only, meaning it's expected in input (POST/PUT)
    # but not shown in output (GET).
    # It takes a list of objects validated by NoteVerseReferenceSerializer.
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
            'id',
            'tag',
            'note_text',
            'verse_references',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, attrs):
        """
        Custom validation to prevent creating duplicate notes for the exact
        same set of verses.
        """
        # This validation is for creation only. For updates, the logic would
        # be more complex (e.g., excluding instance being updated from check).
        if self.instance:
            return attrs  # Skip this validation on updates (PUT/PATCH)

        verse_references = attrs.get('verse_references')
        if not verse_references:
            return attrs

        # Step 1: Resolve verse references to a set of Verse model instances
        verse_instances = []
        for ref in verse_references:
            try:
                verse = Verse.objects.get(
                    book__iexact=ref['book'],
                    chapter=ref['chapter'],
                    verse=ref['verse']
                )
                verse_instances.append(verse)
            except Verse.DoesNotExist:
                # The 'create' method will handle raising a more specific
                # error for this, so we can ignore it here for the purpose
                # of duplicate checking. If a verse doesn't exist, a duplicate
                # set can't exist either.
                pass

        if len(verse_references) != len(verse_instances):
            # Not all provided verse references were valid, so we can't
            # perform a reliable duplicate check. The 'create' method
            # will fail with a proper error message.
            return attrs

        num_verses = len(verse_instances)
        if num_verses == 0:
            return attrs

        # Step 2: Query for existing notes with the exact same set of verses.
        # Find notes that have the same number of verses as the incoming
        # request.
        queryset = Note.objects.annotate(verse_count=Count('verses')).filter(verse_count=num_verses)

        # Further filter this queryset to ensure that for each of our incoming verses,
        # the note is linked to it. This effectively checks for an exact set match.
        for verse in verse_instances:
            queryset = queryset.filter(verses=verse)

        # If any note survives this filtering, it's a duplicate.
        if queryset.exists():
            existing_note_id = queryset.first().id
            raise serializers.ValidationError({
                'verse_references': f"A note with this exact set of verses already exists (ID: {existing_note_id})."
            })

        return attrs

    def create(self, validated_data):
        """
        Overrides the default create method to handle nested verse_references.
        """
        # Pop out the 'verse_references' as it's not a direct field on the Note
        verse_references_data = validated_data.pop('verse_references', [])

        # Create the Note instance using the remaining validated data
        note = Note.objects.create(**validated_data)

        # Handle the many-to-many relationship with verses via NoteVerse
        if verse_references_data:
            note_verse_instances = []
            for verse_ref_data in verse_references_data:
                # Construct the Verse ID based on your 'bible' app's ID format
                # Example: "JOH003016" for John 3:16
                # Ensure the prefix logic matches how your Verse IDs are stored.
                book_prefix = verse_ref_data['book'].upper()[:3]
                verse_id_str = f"{book_prefix}{verse_ref_data['chapter']:03d}{verse_ref_data['verse']:03d}"

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
                        f"{verse_ref_data['verse']}' "
                        f"(Expected ID: {verse_id_str}). "
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

        # Customize tag representation: If a tag is associated, serialize its full details
        # Ensure TagSerializer is imported and available.
        if instance.tag:
            representation['tag'] = TagSerializer(instance.tag).data

        # Customize verses representation: Serialize all associated verses
        # This uses the VerseSerializer from your 'bible' app.
        # Ensure VerseSerializer is imported and available.
        representation['verses'] = VerseSerializer(
            instance.verses.all(),
            many=True
        ).data

        return representation
