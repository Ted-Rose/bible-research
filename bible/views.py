from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Verse
from .serializers import VerseSerializer


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
