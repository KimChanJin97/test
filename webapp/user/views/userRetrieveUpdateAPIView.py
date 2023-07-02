from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    lookup_url_kwarg = "user_id"
    serializer_class = UserSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "유저가 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체를 수정합니다.
        """
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체를 수정합니다.
        """
        return self.update(request, *args, **kwargs)

