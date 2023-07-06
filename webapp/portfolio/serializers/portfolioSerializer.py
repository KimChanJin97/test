from rest_framework import serializers

from portfolio.models import Portfolio, PortfolioAbility, PortfolioTimeline, PortfolioComment
from portfolio.serializers import PortfolioAbilitySerializer, PortfolioCommentSerializer, PortfolioTimelineSerializer


class PortfolioSerializer(serializers.ModelSerializer):
    abilities = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    timeline = serializers.SerializerMethodField()

    def get_abilities(self, obj):
        abilities = PortfolioAbility.objects.filter(portfolio=obj)
        ability_serializer = PortfolioAbilitySerializer(abilities, many=True)
        return ability_serializer.data

    def get_comments(self, obj):
        comments = PortfolioComment.objects.filter(portfolio=obj)
        comment_serializer = PortfolioCommentSerializer(comments, many=True)
        return comment_serializer.data

    def get_timeline(self, obj):
        timelines = PortfolioTimeline.objects.filter(portfolio=obj)
        timeline_serializer = PortfolioTimelineSerializer(timelines, many=True)
        return timeline_serializer.data

    class Meta:
        model = Portfolio
        fields = ['uuid',
                  'user',
                  'representative_image',
                  'description',
                  'certification',
                  'career',
                  'abilities',
                  'comments',
                  'timeline',
                  'git',
                  'instagram',
                  'twitter']
        read_only_fields = [
            'uuid',
            'user',
        ]
