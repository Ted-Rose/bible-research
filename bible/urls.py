from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()

# Register the 'VerseViewSet' with the router.
# This single line handles all standard CRUD operations AND custom actions.
router.register(r'verses', views.VerseViewSet, basename='verse')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
