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
    images = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    like_counts = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = WorkImage.objects.filter(work=obj)
        image_serializer = WorkImageSerializer(images, many=True)
        return image_serializer.data

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

