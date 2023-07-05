from rest_framework.generics import RetrieveDestroyAPIView
from bookmark.models import Bookmark
from bookmark.serializers import BookmarkSerializer
from rest_framework.response import Response


# localhost:8000/works/{work_id}/bookmarks/{work_bookmark_id}
# adder
# work
class WorkBookmarkRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    lookup_url_kwarg = "work_bookmark_uuid"
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def get_object(self):
        user_uuid = self.request.user.uuid
        work_uuid = self.kwargs['work_uuid']
        work_bookmark_uuid = self.kwargs['work_bookmark_uuid']

        try:
            bookmark = Bookmark.objects.get(
                user=user_uuid,
                work=work_uuid,
                uuid=work_bookmark_uuid
            )
            return bookmark
        except Bookmark.DoesNotExist:
            return Response({"error": "북마크가 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - root 페이지의 work 페이지에서 사용됩니다
        - 단일 user 객체의 단일 bookmark 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - root 페이지의 work 페이지에서 사용됩니다
        - 단일 user 객체의 단일 bookmark 객체를 삭제합니다.
        """
        return self.destroy(request, *args, **kwargs)

