from rest_framework import serializers

from work.models import Work, WorkImage


class RootWorkImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = WorkImage
        fields = ['image']


class RootWorkSerializer(serializers.ModelSerializer):
    images = RootWorkImageSerializer(many=True, read_only=True)

    def get_images(self, obj):
        image = obj.image.all()
        return RootWorkImageSerializer(instance=image, many=True, context=self.context).data

    class Meta:
        model = Work
        fields = ['uuid', 'portfolio', 'images']
        read_only_fields = ['uuid', 'portfolio', 'images']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = RootWorkImageSerializer(instance.image.all(), many=True).data
        return representation
