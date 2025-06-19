import uuid
from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()


class Tag(models.Model):
    """
    Represents a user-defined tag for organizing content.
    Tags can be hierarchical (e.g., 'Love' as parent of 'Reckless love').
    """
    # Assuming your original 'id' field is an auto-incrementing primary key.
    # Django will create this automatically as 'id'.
    # If your IDs are like 'TAG00001', you'd use models.CharField(max_length=10, primary_key=True)
    # and manage ID generation yourself or with a custom field.
    # For simplicity, we'll let Django manage it as a default AutoField.

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
        # Ensure a user cannot create two top-level tags with the same name
        # or two child tags with the same name under the same parent.
        # TODO: Add in `unique_together` and `ordering` the 'user'
        unique_together = ('name', 'parent_tag')
        ordering = ['name']

    # def __str__(self):
    #     """
    #     String representation of the Tag.
    #     """
    #     if self.parent_tag:
    #         return f"{self.user.username}'s Tag: {self.parent_tag.name} > {self.name}"
    #     return f"{self.user.username}'s Tag: {self.name}"
