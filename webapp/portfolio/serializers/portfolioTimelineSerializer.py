from rest_framework import serializers

from portfolio.models import PortfolioTimeline


class PortfolioTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioTimeline
        fields = ['uuid',
                  'portfolio',
                  'year',
                  'description']
        read_only_fields = [
            'uuid',
            'portfolio',
        ]