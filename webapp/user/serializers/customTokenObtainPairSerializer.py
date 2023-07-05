from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['uuid'] = str(user.uuid)
        return token


TokenObtainPairSerializer = CustomTokenObtainPairSerializer
