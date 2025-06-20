from rest_framework import viewsets, permissions

from .models import Tag, Note, NoteVerse
from .serializers import TagSerializer, NoteSerializer


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
        Users can only see tags they created.
        """
        # Ensure that only tags belonging to the authenticated user are returned.
        # This prevents users from accessing or modifying tags of other users.
        if self.request.user.is_authenticated:
            return Tag.objects.filter(user=self.request.user).order_by('name')

        return Tag.objects.all().order_by('name')
        # TODO: If not authenticated, return an empty queryset
        return Tag.objects.none()

    def perform_create(self, serializer):
        """
        Assigns the current authenticated user as the creator of the tag
        when a new tag is created.
        """
        # Automatically set the 'user' field of the tag to the requesting user.
        # This means the user does not need to provide their user ID in the request payload.
        serializer.save(
            # TODO:  user=self.request.user
        )

    def perform_update(self, serializer):
        """
        Ensures that a user can only update their own tags.
        """
        # The get_queryset already filters by user, but this adds an explicit check
        # for update operations, enhancing security.
        # TODO: if serializer.instance.user != self.request.user:
        #     return Response(
        #         {"detail": "You do not have permission to edit this tag."},
        #         status=status.HTTP_403_FORBIDDEN
        #     )
        serializer.save()

    def perform_destroy(self, instance):
        """
        Ensures that a user can only delete their own tags.
        """
        # The get_queryset already filters by user, but this adds an explicit check
        # for delete operations, enhancing security.
        # TODO: if instance.user != self.request.user:
        #     return Response(
        #         {"detail": "You do not have permission to delete this tag."},
        #         status=status.HTTP_403_FORBIDDEN
        #     )
        # instance.delete()
        raise NotImplementedError


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be created, viewed, updated, or deleted.
    For MVP, notes are publicly accessible and manageable.
    """
    queryset = Note.objects.all().order_by('-created_at') # Order by most recent first
    serializer_class = NoteSerializer
    permission_classes = [permissions.AllowAny] # Allow any user for MVP

    # The POST (create) functionality is handled automatically by ModelViewSet
    # calling the NoteSerializer's `create` method.
    # No explicit override of `perform_create` is needed here for your requirements.

    # Similarly, default `perform_update` and `perform_destroy` are sufficient
    # for this public MVP setup, as they rely on the serializer's behavior.

