from rest_framework import serializers

from work.models import Work, WorkImage, WorkComment, WorkLike


class WorkImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = WorkImage
        fields = ['image']


class WorkCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkComment
        fields = ['uuid',
                  'work',
                  'writer',
                  'comment',
                  'score',
                  'created_at',
                  ]
        read_only_fields = [
            'uuid',
            'work',
            'writer',
            'created_at',
            'updated_at',
        ]


class WorkLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkLike
        fields = ['uuid', 'work', 'liker', 'created_at']
        read_only_fields = ['uuid', 'work', 'liker', 'created_at', 'updated_at']


class WorkSerializer(serializers.ModelSerializer):
    images = WorkImageSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()
    like_counts = serializers.SerializerMethodField()


    def get_images(self, obj):
        image = obj.image.all()
        return WorkImageSerializer(instance=image, many=True, context=self.context).data

    def get_comments(self, obj):
        comments = WorkComment.objects.filter(work=obj)
        comment_serializer = WorkCommentSerializer(comments, many=True)
        return comment_serializer.data

    def get_like_counts(self, obj):
        likes_count = WorkLike.objects.filter(work=obj).count()
        return likes_count

    class Meta:
        model = Work
        fields = ['uuid', 'portfolio', 'images', 'field', 'description', 'like_counts', 'comments', 'created_at']
        read_only_fields = ['uuid', 'portfolio', 'created_at', 'updated_at']

    def create(self, validated_data):
        instance = Work.objects.create(**validated_data)

        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            WorkImage.objects.create(work=instance, image=image_data)
        return instance

    def update(self, instance, validated_data):
        image_set = self.context['request'].FILES
        if 'image' in image_set:
            instance.image.all().delete()

            for image_data in image_set.getlist('image'):
                WorkImage.objects.create(work=instance, image=image_data)

        # update 오버라이딩했기 때문에 다른 필드들도 로직에 들어가야 함
        instance.field = validated_data.get('field', instance.field)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = WorkImageSerializer(instance.image.all(), many=True).data
        return representation