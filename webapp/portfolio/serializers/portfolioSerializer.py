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

    def update(self, instance, validated_data):
        instance.representative_image = validated_data.get('representative_image', instance.representative_image)
        instance.description = validated_data.get('description', instance.description)
        instance.certification = validated_data.get('certification', instance.certification)
        instance.career = validated_data.get('career', instance.career)
        instance.git = validated_data.get('git', instance.git)
        instance.instagram = validated_data.get('instagram', instance.instagram)
        instance.twitter = validated_data.get('twitter', instance.twitter)

        instance.save()
        return instance
