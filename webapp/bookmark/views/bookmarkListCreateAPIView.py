from rest_framework.generics import ListCreateAPIView

from bookmark.models import Bookmark
from bookmark.serializers import BookmarkSerializer
from work.models import Work


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
        work = self.get_work()
        serializer.save(user=user, work=work)

    def get_work(self):
        work_id = self.kwargs['work_id']
        work = Work.objects.get(pk=work_id)
        return work
