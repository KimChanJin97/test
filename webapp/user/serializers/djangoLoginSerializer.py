from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class DjangoLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'email', 'password', 'thumbnail_image')
