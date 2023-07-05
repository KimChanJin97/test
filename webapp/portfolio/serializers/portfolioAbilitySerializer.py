from rest_framework import serializers

from portfolio.models import PortfolioAbility


class PortfolioAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioAbility
        fields = ['uuid',
                  'portfolio',
                  'ability',
                  'mastery']
        read_only_fields = [
            'uuid',
            'portfolio',
        ]
