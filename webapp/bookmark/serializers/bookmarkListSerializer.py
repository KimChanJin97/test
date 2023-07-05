from rest_framework import serializers
from bookmark.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['uuid', 'user', 'work', 'created_at']
        read_only_fields = ['uuid', 'user', 'work', 'created_at', 'updated_at']
