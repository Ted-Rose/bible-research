import uuid
from django.db import models


def generate_verse_id():
    return f"VER{str(uuid.uuid4()).upper().replace('-', '')[:15]}"


class Verse(models.Model):
    id = models.CharField(
        max_length=18,
        default=generate_verse_id,
        primary_key=True,
        editable=False,
        help_text="Unique identifier for the tag."
    )
    book = models.CharField(max_length=50)
    chapter = models.IntegerField()
    verse = models.IntegerField()

    def __str__(self):
        return f'{self.book} {self.chapter}:{self.verse}'
