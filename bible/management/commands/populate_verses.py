# bible/management/commands/populate_verses.py
from time import sleep
from django.core.management.base import BaseCommand
from bible.services import get_passage_data, ESVApiError
from bible.models import Verse

class Command(BaseCommand):
    help = 'Populates the database with Bible verses from the ESV API.'

    def handle(self, *args, **kwargs):
        """
        The main logic of the management command.
        """
        self.stdout.write(self.style.SUCCESS("Starting Bible population script..."))

        # Clear existing verses to prevent duplicates on re-runs
        self.stdout.write("Deleting old verse data...")
        Verse.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Old data cleared."))

        # This should be a predefined list of all books in the Bible
        # For this example, we'll use a small subset.
        books_to_fetch = ["Genesis", "John"]
        
        for book in books_to_fetch:
            self.stdout.write(f"\nProcessing book: {book}")
            current_chapter = 1
            while True:
                try:
                    passage_query = f"{book} {current_chapter}"
                    self.stdout.write(f"  Fetching {passage_query}...")
                    
                    data = get_passage_data(passage_query, format='json')
                    
                    # Extract verses and create model instances
                    verses_to_create = []
                    passage_text = data['passages'][0]
                    canonical = data['canonical']
                    
                    # This is a simplified parsing logic. The actual API response
                    # may require more complex parsing to split verses correctly.
                    # For this example, we assume one verse per line.
                    lines = passage_text.strip().split('\n')
                    for line in lines:
                        if not line.strip():
                            continue
                        
                        try:
                            verse_num_str, text = line.strip().split(' ', 1)
                            verse_num = int(verse_num_str)
                            
                            # Construct a unique ID
                            verse_id = f"{book.upper()[:3]}{current_chapter:03d}{verse_num:03d}"
                            
                            verses_to_create.append(
                                Verse(
                                    id=verse_id,
                                    book=book,
                                    chapter=current_chapter,
                                    verse=verse_num,
                                    text=text
                                )
                            )
                        except (ValueError, IndexError):
                            self.stdout.write(self.style.WARNING(f"    Could not parse line: '{line}'"))
                            continue

                    Verse.objects.bulk_create(verses_to_create)
                    self.stdout.write(self.style.SUCCESS(f"    Successfully saved {len(verses_to_create)} verses for {passage_query}."))

                    # Check if there is a next chapter in the same book
                    next_chapter_ref = data['passage_meta'][0].get('next_chapter')
                    if next_chapter_ref and next_chapter_ref[0] == book:
                        current_chapter = next_chapter_ref[1]
                        sleep(1) # Be respectful to the API
                    else:
                        self.stdout.write(f"Finished processing all chapters for {book}.")
                        break # Exit the while loop for this book

                except ESVApiError as e:
                    self.stdout.write(self.style.ERROR(f"  API Error for {passage_query}: {e}"))
                    self.stdout.write(f"  Moving to the next book.")
                    break # Exit the while loop and move to the next book
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"  An unexpected error occurred: {e}"))
                    break

        self.stdout.write(self.style.SUCCESS("\nBible population script finished."))

