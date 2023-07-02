from rest_framework import serializers

from portfolio.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id',
                  'user',
                  'representative_image',
                  'description',
                  'certification',
                  'career',
                  'git',
                  'instagram',
                  'twitter']
        read_only_fields = [
            'id',
            'user',
        ]