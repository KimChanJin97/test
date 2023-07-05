from rest_framework.generics import RetrieveDestroyAPIView
from bookmark.models import Bookmark
from bookmark.serializers import BookmarkSerializer
from rest_framework.response import Response


# localhost:8000/bookmarks/{root_bookmark_id}
# adder
# work
class RootBookmarkRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    lookup_url_kwarg = "root_bookmark_uuid"
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def get_object(self):
        user_uuid = self.request.user.uuid
        root_bookmark_uuid = self.kwargs['root_bookmark_uuid']

        try:
            bookmark = Bookmark.objects.get(
                user=user_uuid,
                uuid=root_bookmark_uuid
            )
            return bookmark
        except Bookmark.DoesNotExist:
            return Response({"error": "북마크가 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - root 페이지에 사용됩니다.
        - 단일 user 객체의 단일 bookmark 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     """
    #     [ 설명 ]
    #     - 단일 user 객체의 단일 bookmark 객체를 수정합니다.
    #     """
    #     return self.partial_update(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     """
    #     [ 설명 ]
    #     - 단일 user 객체의 단일 bookmark 객체를 수정합니다.
    #     """
    #     return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - root 페이지의 bookmark 페이지에서 사용됩니다.
        - 단일 user 객체의 단일 bookmark 객체를 삭제합니다.
        """
        return self.destroy(request, *args, **kwargs)

    # def perform_update(self, serializer):
    #     adder = self.request.user
    #     work = self.get_work()
    #     serializer.save(adder=adder, work=work)
    #
    # def get_work(self):
    #     work_id = self.kwargs['work_id']
    #     try:
    #         work = Work.objects.get(id=work_id)
    #         return work
    #     except Work.DoesNotExist:
    #         return Response({"error": "작업물이 존재하지 않습니다."})
