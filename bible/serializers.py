import logging
from rest_framework import serializers
from .models import Verse
from bible.services.dbt.client import DBTClient

logger = logging.getLogger(__name__)


class VerseSerializer(serializers.ModelSerializer):
    """
    Serializes Verse model data into JSON format.
    """
    class Meta:
        model = Verse
        # The 'fields' attribute specifies which model fields to include in the API output.
        fields = ['id', 'book', 'chapter', 'verse', 'text']
        read_only_fields = ['id']


class BiblePassageSerializer(serializers.Serializer):
    book = serializers.CharField(
      required=True,
      help_text="Standard book ID (e.g., '2CH')"
    )
    book_name = serializers.CharField(
      required=False,
      help_text="Full book name (e.g., '2 Chronicles')"
    )
    chapter = serializers.IntegerField(
      required=True,
      min_value=1,
      help_text="Chapter number"
    )

    def to_representation(self, instance):
        dbt_client = DBTClient()
        book_id = instance.get('book')
        book_name = instance.get('book_name', '')
        chapter = str(instance.get('chapter'))

        try:
            verses_data = dbt_client.get_verses(book_id, chapter)

            if verses_data and 'data' in verses_data and verses_data['data']:
                response_data = {
                    'book': book_id,
                    'book_name': book_name,
                    'chapter': int(chapter),
                    'verses': [
                        {
                            'verse': verse['verse_start'],
                            'text': verse['verse_text']
                        }
                        for verse in verses_data['data']
                    ]
                }

                return response_data

            return {
                'book': book_id,
                'book_name': book_name,
                'chapter': int(chapter),
                'verses': [],
                'message': 'No verses found for the specified passage'
            }

        except Exception as e:
            logger.error(f"Error fetching Bible passage: {str(e)}")
            return {
                'book': book_id,
                'book_name': book_name,
                'chapter': int(chapter),
                'error': str(e)
            }
