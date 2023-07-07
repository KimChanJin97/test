from rest_framework import serializers

from work.models import WorkImage


class WorkImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = WorkImage
        fields = ['image']