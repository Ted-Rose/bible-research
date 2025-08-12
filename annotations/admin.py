from django.contrib import admin
from .models import Tag, Note, NoteVerse


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Tag model.
    """
    list_display = ('name', 'parent_tag', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at', 'parent_tag')
    # Use a raw input for parent_tag for better UX with many tags
    raw_id_fields = ('parent_tag',)

    # Optionally, you can add fields or fieldsets to customize the edit form
    fieldsets = (
        (None, {
            'fields': ('name', 'parent_tag',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # Makes this section collapsible
        }),
    )
    # These fields should not be editable by admin users
    readonly_fields = ('created_at', 'updated_at',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Note model.
    """
    list_display = ('id', 'user', 'note_text', 'created_at', 'updated_at')
    search_fields = ('note_text',)
    list_filter = ('created_at', 'updated_at', 'user')
    raw_id_fields = ('user',)

    fieldsets = (
        (None, {
            'fields': ('user', 'note_text', 'tag')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at',)


@admin.register(NoteVerse)
class NoteVerseAdmin(admin.ModelAdmin):
    """
    Admin configuration for the NoteVerse model.
    """
    list_display = ('id', 'note', 'verse', 'created_at')
    search_fields = ('note__content', 'verse__text')
    list_filter = ('created_at',)
    raw_id_fields = ('note', 'verse')

    readonly_fields = ('created_at',)
