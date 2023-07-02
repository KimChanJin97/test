from rest_framework import fields, serializers
from user.models import User, INTERESTS


class UserSerializer(serializers.ModelSerializer):
    field = fields.MultipleChoiceField(choices=INTERESTS)

    class Meta:
        model = User
        fields = ['user_id', 'kakaoId', 'kakao_thumbnail_url', 'thumbnail_image', 'email', 'name', 'phone_number',
                  'birth_date', 'field', 'job', 'univ', 'major', 'univ_identification', 'univ_email']
        read_only_fields = ['user_id', 'kakaoId', 'email', 'kakao_thumbnail_url',]

