from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class DjangoRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'thumbnail_image')

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        thumbnail_image = validated_data.get('thumbnail_image')
        user = User(email=email, thumbnail_image=thumbnail_image,)
        user.set_password(password)
        user.save()
        return user


