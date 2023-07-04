from rest_framework import serializers

from outsourcing.models import OutsourcingComment


class OutsourcingCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutsourcingComment
        fields = ['id',
                  'outsourcing',
                  'writer',
                  'comment',
                  'score',
                  'created_at',
                  ]
        read_only_fields = [
            'id',
            'outsourcing',
            'writer',
            'created_at',
            'updated_at',
        ]

