from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from .models import Verse
from .serializers import VerseSerializer, BiblePassageSerializer
from bible.services.dbt.client import DBTClient
from .utils.bible_books import get_dbt_book_id


class VerseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', None)
        if not query:
            return Response(
                {"error": "A search query parameter 'q' is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        results = "Some results"
        return Response(results)


class BiblePassageView(APIView):
    """
    API endpoint to retrieve Bible passages.
    Example: /api/v1/bible/?passage=2%20Chronicles%2014
    """

    def get(self, request, format=None):
        passage = request.query_params.get('passage')
        if not passage:
            return Response(
                {"error": "Passage parameter is required. Example: ?passage=John+3:16"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            parts = passage.split()
            if len(parts) < 2:
                raise ValueError("Invalid passage format. Use 'Book Chapter' (e.g., 'John 3')")

            # The book name might have spaces (e.g., "1 John")
            chapter_part = parts[-1]
            book_name = ' '.join(parts[:-1])

            # Convert book name to standard book ID
            book_id = get_dbt_book_id(book_name)
            if not book_id:
                raise ValueError(f"Unknown book: {book_name}")

            try:
                chapter = int(chapter_part)
                if chapter <= 0:
                    raise ValueError("Chapter must be a positive number")
            except ValueError:
                raise ValueError("Chapter must be a valid number")

            data = {
                'book': book_id,
                'book_name': book_name,
                'chapter': chapter
            }

            serializer = BiblePassageSerializer(data=data)
            if serializer.is_valid():
                return Response(serializer.to_representation(data))
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
