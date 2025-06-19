import uuid
from django.db import models
from django.db.models import UniqueConstraint, Q
from bible.models import Verse 
# from django.contrib.auth import get_user_model

# User = get_user_model()


class Tag(models.Model):
    """
    Represents a user-defined tag for organizing content.
    Tags can be hierarchical (e.g., 'Love' as parent of 'Reckless love').
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                          help_text="Unique identifier for the tag.")
    # user = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name='tags',
    #     help_text="The user who created this tag."
    # )
    name = models.CharField(
        max_length=100,
        # Users can have tags with the same name, but not for the same user.
        unique=False,
        help_text="The name of the tag (e.g., 'Love', 'Grace')."
    )
    parent_tag = models.ForeignKey(
        # Refers to the Tag model itself, allowing for hierarchical tags.
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,  # The parent_tag is optional.
        related_name='children',
        help_text="The parent tag in a hierarchical structure (optional)."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            uuid_str = str(uuid.uuid4()).upper().replace('-', '')
            self.id = f"TAG{uuid_str[:12]}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

        # TODO: Ensure user cannot create two top-level tags with the same name
        # or two child tags with the same name under the same parent.
        # Replace first two `constraints` with this when users added:
        # unique_together = ('user', 'name', 'parent_tag')
        # ordering = ['name']

        constraints = [
            # Ensures unique 'name' for top-level tags (when parent_tag NULL)
            UniqueConstraint(
                fields=['name'],
                condition=Q(parent_tag__isnull=True),
                name='unique_top_level_tag_name'
            ),
            # Ensures 'name' is unique for child tags under the same parent
            UniqueConstraint(
                fields=['name', 'parent_tag'],
                condition=Q(parent_tag__isnull=False),
                name='unique_child_tag_name_per_parent'
            ),
        ]

    # def __str__(self):
    #     """
    #     String representation of the Tag.
    #     """
    #     if self.parent_tag:
    #         return f"{self.user.username}'s Tag: {self.parent_tag.name} > {self.name}"
    #     return f"{self.user.username}'s Tag: {self.name}"


class Note(models.Model):
    """
    Represents a user's personal note or commentary.
    Notes can be associated with a primary tag.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                          help_text="Unique identifier for the note.")

    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        # Allows you to get notes from a Tag object (e.g., my_tag.notes.all())
        related_name='notes',
        help_text="A primary tag associated with this note (optional)."
    )

    note_text = models.TextField(
        help_text="The actual content of the note."
    )

    # Many-to-many relationship with Verse model, through the NoteVerse
    # intermediary table. This explicit 'through' model is necessary because
    # you have 'note_verses' table in your schema, which implies additional
    # data (like 'id' for the link).
    verses = models.ManyToManyField(
        Verse,
        through='NoteVerse',
        # Allows you to get notes from a Verse object
        # (e.g., my_verse.notes.all())
        related_name='notes',
        help_text="The Bible verses associated with this note."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        # Order by most recent notes first
        ordering = ['-created_at']

    def __str__(self):
        # Display the first 50 characters of the note text
        truncated_text = self.note_text[:50]
        ellipsis = '...' if len(self.note_text) > 50 else ''
        return f"Note (ID: {self.id.hex[:8]}): {truncated_text}{ellipsis}"


class NoteVerse(models.Model):
    """
    Intermediary model for many-to-many relationship between Note and Verse.
    This explicit model corresponds to your 'note_verses' table.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                          help_text="Unique identifier for the note-verse link.")

    note = models.ForeignKey(
        Note,
        on_delete=models.CASCADE, # If a note is deleted, its links to verses are also deleted.
        help_text="The note associated with the verse."
    )

    verse = models.ForeignKey(
        Verse,
        on_delete=models.PROTECT,  # Prevent deleting Verses that have Notes
        help_text="The verse associated with the note."
    )

    created_at = models.DateTimeField(auto_now_add=True) # Useful for tracking when the link was made

    class Meta:
        verbose_name = "Note-Verse Link"
        verbose_name_plural = "Note-Verse Links"
        # Ensures that a specific note is linked to a specific verse only once.
        unique_together = ('note', 'verse')
        ordering = ['note', 'verse']

    def __str__(self):
        return f"Link: Note {self.note.id.hex[:8]} to Verse {self.verse.id}"
