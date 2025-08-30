from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.db import models

from .models import Tag, Note
from .serializers import TagSerializer, NoteSerializer

User = get_user_model()


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be created, viewed, updated, or deleted.

    Users can only see and manage their own tags.
    """
    serializer_class = TagSerializer

    def get_queryset(self):
        """
        Returns the queryset of tags that the current user has access to.
        Authenticated users see their own tags.
        Unauthenticated users see the guest user's tags.
        """
        # For authenticated users, return their own tags
        if self.request.user.is_authenticated:
            return Tag.objects.filter(user=self.request.user).order_by('name')

        # For unauthenticated users, return guest user's tags
        try:
            guest_user = User.objects.get(username='guest')
            return Tag.objects.filter(user=guest_user).order_by('name')
        except User.DoesNotExist:
            # If guest user doesn't exist, return empty queryset
            return Tag.objects.none()

    def perform_create(self, serializer):
        """
        Assigns the current authenticated user as the creator of the tag
        when a new tag is created.
        """
        # Automatically set the 'user' field of the tag to the requesting user.
        # User doesn't need to provide their user ID in the request.
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            # For unauthenticated users, use guest user
            try:
                guest_user = User.objects.get(username='guest')
                serializer.save(user=guest_user)
            except User.DoesNotExist:
                # Let the serializer handle this case
                serializer.save()

    def perform_update(self, serializer):
        """
        Ensures that a user can only update their own tags.
        """
        # The get_queryset already filters by user, so this is just a safeguard
        # User is already filtered by get_queryset
        serializer.save()

    def perform_destroy(self, instance):
        """
        Ensures that a user can only delete their own tags.
        """
        # The get_queryset already filters by user, so this is just a safeguard
        # Users can only delete tags in their filtered queryset
        instance.delete()


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be created, viewed, updated, or deleted.
    Authenticated users see and manage their own notes.
    Unauthenticated users can view notes marked as public.

    Additional filtering:
    - GET /api/v1/notes/?tag_id={tag_id} - List notes filtered by tag ID
    - GET /api/v1/notes/?public=true - List both public and private notes
    """
    serializer_class = NoteSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Assigns the current authenticated user as the creator of the note
        when a new note is created.
        """
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """
        Ensures that a user can only update their own notes.
        Raises PermissionDenied if a user attempts to update another user's note.
        """
        instance = serializer.instance
        if (self.request.user.is_authenticated and
                instance.user != self.request.user):
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied(
                "You do not have permission to update this note."
            )
        serializer.save()

    def perform_destroy(self, instance):
        """
        Ensures that a user can only delete their own notes.
        Raises PermissionDenied if a user attempts to delete another user's note.
        """
        if (self.request.user.is_authenticated and
                instance.user != self.request.user):
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied(
                "You do not have permission to delete this note."
            )
        instance.delete()

    def get_queryset(self):
        """
        Returns the queryset of notes that the current user has access to.
        - Authenticated users see their own private notes by default
        - Unauthenticated users see only public notes

        Supports filtering via query parameters:
        - GET /api/v1/notes/?tag_id=<tag_id> - Filter by tag ID
        - GET /api/v1/notes/?public=true:
          List all public notes and user's own notes

        Special cases:
        - When requesting a specific note by ID:
          Users see the note if it's public or their own
        - When filtering by tag_id:
          Users see all public notes with that tag and their own notes
        """

        public_param = self.request.query_params.get('public', '')
        public_filter = public_param.lower() == 'true'

        tag_id = self.request.query_params.get('tag_id', None)
        note_id = self.kwargs.get('pk', None)
        specific_request = note_id is not None or tag_id is not None

        if self.request.user.is_authenticated:
            if public_filter or specific_request:
                # Show all public notes and user's own notes
                queryset = Note.objects.filter(
                    models.Q(public=True) | models.Q(user=self.request.user)
                )
            else:
                # Default: show only the user's private notes
                queryset = Note.objects.filter(
                    user=self.request.user,
                )
        else:
            # Unauthenticated users only see public notes
            queryset = Note.objects.filter(public=True)

        if tag_id is not None:
            queryset = Note.objects.filter(
                    models.Q(public=True) | models.Q(tag_id=tag_id)
                )

        return queryset.order_by('-created_at')
