from rest_framework import serializers

from portfolio.models import Portfolio


class PortfolioCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['portfolio',
                  'writer',
                  'comment',
                  'score',
                  ]
        read_only_fields = [
            'user',
            'writer',
        ]
