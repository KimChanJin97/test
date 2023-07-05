from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from bookmark.serializers import BookmarkSerializer
from bookmark.models import Bookmark
from work.models import Work

# localhost:8000/works/{work_uuid}/bookmarks/
# adder
# work
class WorkBookmarkListCreateAPIView(ListCreateAPIView):
    serializer_class = BookmarkSerializer
    ordering = ['created_at']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Bookmark.objects.none()

        user_uuid = self.request.user.uuid
        work_uuid = self.kwargs['work_uuid']

        queryset = Bookmark.objects.filter(
            user=user_uuid,
            work=work_uuid
        )
        return queryset

    def get(self, request, *args, **kwargs):
        """
        단일 user 객체의 단일 portfolio 객체의 모든 outsourcing 객체들을 조회합니다.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - root 페이지의 work 페이지에서 사용됩니다
        - 단일 user 객체의 단일 bookmark 객체를 생성합니다.
        """
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        work = self.get_work()
        serializer.save(work=work, user=user)

    def get_work(self):
        work_uuid = self.kwargs['work_uuid']
        try:
            work = Work.objects.get(
                uuid=work_uuid
            )
            return work
        except Work.DoesNotExist:
            return Response({"error": "작업물이 존재하지 않습니다."})

