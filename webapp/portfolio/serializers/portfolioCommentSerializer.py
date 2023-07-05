from rest_framework import serializers

from portfolio.models import PortfolioComment


class PortfolioCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioComment
        fields = ['uuid',
                  'portfolio',
                  'writer',
                  'comment',
                  'score',
                  ]
        read_only_fields = [
            'uuid',
            'portfolio',
            'writer',
        ]
