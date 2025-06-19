from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    """
    Serializes Tag model data for API input and output.
    Includes the 'parent_tag' as its primary key for relationships.
    """
    parent_tag = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Tag
        fields = [
            'id',
            # 'user',
            'name',
            'parent_tag',
            'created_at',
            'updated_at',
        ]
        # 'read_only_fields' makes sure 'id', 'created_at', 'updated_at' are
        # automatically handled by Django and not expected in user input.
        read_only_fields = ['id', 'created_at', 'updated_at']
