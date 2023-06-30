from rest_framework import serializers

from field.models import Field


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['id']

    def to_representation(self, instance):
        return instance.id
