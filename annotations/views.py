from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model

from .models import Tag, Note
from .serializers import TagSerializer, NoteSerializer

User = get_user_model()


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be created, viewed, updated, or deleted.

    Users can only see and manage their own tags.
    """
    serializer_class = TagSerializer
    # permission_classes = [permissions.IsAuthenticated]

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
    Unauthenticated users see and manage the guest user's notes.
    """
    serializer_class = NoteSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Returns the queryset of notes that the current user has access to.
        Authenticated users see their own notes.
        Unauthenticated users see the guest user's notes.
        """
        # For authenticated users, return their own notes
        if self.request.user.is_authenticated:
            return Note.objects.filter(
                user=self.request.user
            ).order_by('-created_at')

        # For unauthenticated users, return guest user's notes
        try:
            # TODO: Remove guest logic in rhis file as it is handled in middleware
            guest_user = User.objects.get(username='guest')
            return Note.objects.filter(user=guest_user).order_by('-created_at')
        except User.DoesNotExist:
            # If guest user doesn't exist, return empty queryset
            return Note.objects.none()

    def perform_create(self, serializer):
        """
        Assigns the current authenticated user as the creator of the note
        when a new note is created.
        """
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

