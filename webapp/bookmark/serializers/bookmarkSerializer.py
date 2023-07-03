from rest_framework import serializers
from bookmark.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['adder', 'work', 'created_at']
        read_only_fields = ['adder', 'created_at', 'updated_at']
