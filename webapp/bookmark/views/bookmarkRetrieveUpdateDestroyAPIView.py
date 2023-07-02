from rest_framework.generics import RetrieveUpdateDestroyAPIView
from bookmark.models import Bookmark
from bookmark.serializers import BookmarkSerializer
from rest_framework.response import Response
from work.models import Work


class BookmarkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = "bookmark_id"
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 bookmark 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 bookmark 객체를 수정합니다.
        """
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 bookmark 객체를 수정합니다.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 bookmark 객체를 삭제합니다.
        """
        return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        user = self.request.user
        work_id = self.request.data.get('work')
        try:
            work = Work.objects.get(id=work_id)
            serializer.save(user=user, work=work)
        except Work.DoesNotExist:
            return Response({"error": "존재하지 작업물입니다."})

        serializer.save()
