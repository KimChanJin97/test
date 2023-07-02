from rest_framework import serializers

from portfolio.models import Portfolio


class PortfolioAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['portfolio',
                  'ability',
                  'mastery']
        read_only_fields = [
            'portfolio'
        ]
