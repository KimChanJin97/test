from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from user.serializers import UserSerializer
from user.models import User


# TODO: 실제로는 사용하지 않음. 모든 유저 객체 확인용
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 모든 user 객체를 조회합니다.
        """
        return self.list(request, *args, **kwargs)



