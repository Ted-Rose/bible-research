from rest_framework import serializers
from .models import Verse

class VerseSerializer(serializers.ModelSerializer):
    """
    Serializes Verse model data into JSON format.
    """
    class Meta:
        model = Verse
        # The 'fields' attribute specifies which model fields to include in the API output.
        fields = ['id', 'book', 'chapter', 'verse', 'text']
