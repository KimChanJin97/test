from rest_framework import serializers

from work.models import WorkComment


class WorkCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkComment
        fields = ['id',
                  'work',
                  'writer',
                  'comment',
                  'score',
                  'created_at',
                  ]
        read_only_fields = [
            'id',
            'work',
            'writer',
            'created_at',
            'updated_at',
        ]