from rest_framework import serializers

from portfolio.models import Portfolio
from work.models import Work, WorkImage
from field.models import Field


class WorkImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = WorkImage
        fields = ['image']


class WorkSerializer(serializers.ModelSerializer):
    images = WorkImageSerializer(many=True, read_only=True)

    def get_images(self, obj):
        image = obj.image.all()
        return WorkImageSerializer(instance=image, many=True, context=self.context).data

    class Meta:
        model = Work
        fields = ['id', 'portfolio', 'field', 'images', 'description', 'created_at']
        read_only_fields = ['id', 'portfolio', 'field', 'images', 'description', 'created_at', 'updated_at']

    def create(self, validated_data):
        portfolio_id = self.context['view'].kwargs.get('portfolio_id')
        try:
            portfolio = Portfolio.objects.get(id=portfolio_id)
        except Portfolio.DoesNotExist:
            raise serializers.ValidationError("존재하지 않는 포트폴리오입니다.")

        field_id = self.context['request'].data.get('field')  # Field ID 가져오기

        if not field_id:
            raise serializers.ValidationError("필드를 선택해야 합니다.")

        try:
            field = Field.objects.get(id=field_id)  # Field 인스턴스 가져오기
        except Field.DoesNotExist:
            raise serializers.ValidationError("존재하지 않는 필드입니다.")

        validated_data['portfolio'] = portfolio
        validated_data['field'] = field

        instance = Work.objects.create(**validated_data)

        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            WorkImage.objects.create(work=instance, image=image_data)
        return instance

    def update(self, instance, validated_data):
        # Update the fields of the instance
        instance.description = validated_data.get('description', instance.description)

        # Handle changes to the field field
        field_id = self.context['request'].data.get('field')
        if field_id:
            try:
                field = Field.objects.get(id=field_id)
                instance.field = field
            except Field.DoesNotExist:
                raise serializers.ValidationError("존재하지 않는 필드입니다.")

        # Handle changes to the image field
        image_set = self.context['request'].FILES
        if 'image' in image_set:
            # Delete the existing images
            instance.image.all().delete()

            # Create new images
            for image_data in image_set.getlist('image'):
                WorkImage.objects.create(work=instance, image=image_data)

        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = WorkImageSerializer(instance.image.all(), many=True).data
        return representation
