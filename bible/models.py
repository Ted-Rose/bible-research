import uuid
from django.db import models
from bible_research.utils import generate_id


class Verse(models.Model):
    id = models.CharField(
        max_length=18,
        default=f"VER{str(uuid.uuid4()).upper().replace('-', '')[:15]}",
        primary_key=True,
        editable=False,
        help_text="Unique identifier for the tag."
    )
    book = models.CharField(max_length=50)
    chapter = models.IntegerField()
    verse = models.IntegerField()

    def __str__(self):
        return f'{self.book} {self.chapter}:{self.verse}'
