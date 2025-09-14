from django.core.management.base import BaseCommand
from django.db.models import Count
from pathlib import Path
import json
from bible.models import Verse


class Command(BaseCommand):
    help = 'Extract book information from JSON and database'

    def handle(self, *args, **options):
        # Get the directory where this script is located
        script_dir = Path(__file__).resolve().parent.parent.parent.parent.parent / 'bible_research' / 'bible' / 'services' / 'dbt' / 'books'
        json_path = script_dir / "esv.json"

        try:
            # Input data
            self.stdout.write(f"Looking for JSON file at: {json_path}")
            with open(json_path, "r") as f:
                data = json.load(f)

            # Create and print the mapping from JSON
            result = {book["name"]: book["book_id"] for book in data["books"]}
            self.stdout.write("\nBooks from JSON:")
            self.stdout.write(json.dumps(result, indent=2))

            # Get and print unique books from database
            unique_books = list(Verse.objects.values('book')
                              .annotate(count=Count('book'))
                              .order_by('book'))

            self.stdout.write("\nUnique books from database:")
            self.stdout.write(json.dumps(unique_books, indent=2))

            book_mapping = {book["name"]: book["book_id"] for book in data["books"]}
            print(book_mapping)

            # Replace the for loop with this:
            for book_data in unique_books:
                book_name = book_data["book"]
                # Handle the special case for Song of Songs
                if book_name == "Song of Songs":
                    book_name = "The Song of Solomon"

                book_id = book_mapping.get(book_name)
                if book_id:
                    # Update all verses with this book name
                    updated_count = Verse.objects.filter(book=book_data["book"]).update(dbt_book_id=book_id)
                    self.stdout.write(
                      f"Updated {book_data['book']} ({updated_count} verses) \
                        with ID: {book_id}")
                else:
                    self.stderr.write(
                      f"Warning: No mapping found for book:\
                        {book_data['book']}")

        except FileNotFoundError:
            self.stderr.write(f"Error: Could not find {json_path}")
            self.stderr.write(f"Current working directory: {Path.cwd()}")
            self.stderr.write(f"Script directory: {script_dir}")
            self.stderr.write("Please make sure esv_books.json exists in the script directory")
        except Exception as e:
            self.stderr.write(f"An error occurred: {str(e)}")