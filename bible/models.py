import uuid
from django.db import models


class Verse(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    book = models.CharField(max_length=50)
    chapter = models.IntegerField()
    verse = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            uuid_str = str(uuid.uuid4()).upper().replace('-', '')
            self.id = f"VER{uuid_str[:15]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.book} {self.chapter}:{self.verse}'
