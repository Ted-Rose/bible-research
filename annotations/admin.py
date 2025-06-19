from django.contrib import admin
from .models import Tag

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
