from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Verse
from .serializers import VerseSerializer
from .services import search_passages, ESVApiError


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
        try:
            results = search_passages(query)
            return Response(results)
        except ESVApiError as e:
            return Response(
                {"error": f"An API error occurred: {e}"},
                status=status.HTTP_502_BAD_GATEWAY
            )
