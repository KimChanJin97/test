from rest_framework import serializers

from tag.models import Keyword


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id', 'tag']

    def to_representation(self, instance):
        return instance.keyword
