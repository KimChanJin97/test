from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"

    def get_object(self):
        user_id = self.kwargs['user_id']
        try:
            user = User.objects.get(pk=user_id)
            return user
        except user.DoesNotExist:
            return Response({"error": "존재하지 않는 유저입니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체를 수정합니다.
        - form-data 로 patch 요청을 보내야 합니다.
        - 1차 로그인 이후 user 객체를 수정하는 함수입니다.
        - 때문에 모든 필드는 Null=True 입니다.
        - univ_identification 이미지는 여러 개 보낼 수 있습니다.
        """
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체를 수정합니다.
        - form-data 로 put 요청을 보내야 합니다.
        - 1차 로그인 이후 user 객체를 수정하는 함수입니다.
        - 때문에 모든 필드는 Null=True 입니다.
        - univ_identification 이미지는 여러 개 보낼 수 있습니다.
        """
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
