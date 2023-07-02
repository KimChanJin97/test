from rest_framework import serializers

from outsourcing.models import Outsourcing


class OutsourcingCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outsourcing
        fields = ['id',
                  'portfolio',
                  'writer',
                  'comment',
                  'score',
                  'created_at',
                  ]
        read_only_fields = [
            'id',
            'portfolio',
            'writer',
            'created_at',
            'updated_at',
        ]

