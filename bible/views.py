from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Verse
from .serializers import VerseSerializer
from bible.services.dbt.client import DBTClient


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

    # @action(detail=False, methods=['get'], url_path='passage')
    # def verses(self, request):
    #     """
    #     Get verses for a specific Bible passage.
    #     Example: /api/v1/verses/passage/?passage=John+3:16
    #     """
    #     passage = request.query_params.get('passage')
    #     if not passage:
    #         return Response(
    #             {"error": "A passage parameter is required (e.g., ?passage=John+3:16)"},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #     client = DBTClient()
    #     verses = client.get_verses(passage)
    #     return Response({
    #         "passage": passage,
    #         "verses": verses
    #     })
