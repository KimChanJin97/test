from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from bookmark.models import Bookmark
from bookmark.serializers import BookmarkSerializer
from work.models import Work
from user.models import User


class BookmarkListCreateAPIView(ListCreateAPIView):
    serializer_class = BookmarkSerializer
    ordering = ['id']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Bookmark.objects.none()
        user_id = self.kwargs['user_id']
        queryset = Bookmark.objects.filter(user_id=user_id).order_by('id')

        return queryset

    def get(self, request, *args, **kwargs):
        """
        단일 유저 객체의 모든 북마크 객체들을 조회합니다.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        단일 유저 객체의 단일 북마크 객체을 생성합니다.
        """
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        work_id = self.request.data.get('work')
        try:
            work = Work.objects.get(id=work_id)
            serializer.save(user=user, work=work)
        except Work.DoesNotExist:
            return Response({"error": "존재하지 작업물입니다."})

