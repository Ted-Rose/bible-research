from django.core.management.base import BaseCommand
import json
from bible.models import Verse
from datetime import datetime


class Command(BaseCommand):
    help = 'Populate the Verse model from the ESV Bible verses JSON file'

    def handle(self, *args, **kwargs):
        start_time = datetime.now()
        print(f'Starting ESV Bible verses import at {start_time}')

        try:
            populate_verses()
            end_time = datetime.now()
            print(f'ESV Bible verses import completed successfully at {end_time}')
            print(f'Total time taken: {end_time - start_time}')
        except Exception as e:
            print(f'Error importing ESV Bible verses: {e}')


def populate_verses():
    with open('bible/esv_bible_verses.json') as f:
        data = json.load(f)

    for book, book_data in data.items():
        chapters = book_data['chapters']

        for chapter, chapter_data in chapters.items():
            verse_count = chapter_data['verse_count']

            for verse in range(1, int(verse_count) + 1):
                # Perform commit per verse to check db performance (for fun)
                verse_obj = Verse(
                    book=book,
                    chapter=int(chapter),
                    verse=verse
                )
                verse_obj.save()
