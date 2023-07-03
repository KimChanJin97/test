from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from bookmark.serializers import BookmarkSerializer
from work.models import Work


# localhost:8000/works/{work_id}/bookmarks/
# adder
# work
class RootBookmarkCreateAPIView(CreateAPIView):
    serializer_class = BookmarkSerializer
    ordering = ['id']

    def post(self, request, *args, **kwargs):
        """
        단일 유저 객체의 단일 북마크 객체을 생성합니다.
        """
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        adder = self.request.user
        work = self.get_work()
        serializer.save(adder=adder, work=work)

    def get_work(self):
        work_id = self.kwargs['work_id']
        try:
            work = Work.objects.get(id=work_id)
            return work
        except Work.DoesNotExist:
            return Response({"error": "작업물이 존재하지 않습니다."})

