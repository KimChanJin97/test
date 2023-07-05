from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import DjangoLoginSerializer, CustomTokenObtainPairSerializer


class DjangoLoginAPIView(APIView):

    def post(self, request):
        """
        [ 설명 ]
        - email과 password 를 넣고 post 요청하면 로그인됩니다.
        - DB에 존재하는 유저라면 해당 유저의 access 토큰과 refresh 토큰을 응답에 실어 보냅니다.
        """
        user = authenticate(
            email=request.data.get("email"), password=request.data.get("password")
        )
        if user is not None:
            serializer = DjangoLoginSerializer(user)
            token = CustomTokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
