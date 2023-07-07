from rest_framework import serializers

from work.models import Work


class RootWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['uuid', 'portfolio', 'image']
        read_only_fields = ['uuid', 'portfolio', 'image']
