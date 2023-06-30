from rest_framework import status
from rest_framework.generics import RetrieveDestroyAPIView
from bookmark.models import Bookmark
from bookmark.serializers import BookmarkSerializer
from rest_framework.response import Response


class BookmarkRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    lookup_url_kwarg = "bookmark_id"
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def get_object(self):
        bookmark_id = self.kwargs['Bookmark_id']
        try:
            bookmark = Bookmark.objects.get(pk=bookmark_id)
            return bookmark
        except bookmark.DoesNotExist:
            return Response({"error": "존재하지 않는 북마크입니다."})

    def get(self, request, *args, **kwargs):
        """
        get을 호출하면 retrieve가 호출됩니다.
        단일 user 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        단일 user 객체를 조회합니다.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """
        delete를 호출하면 destroy가 호출됩니다.
        단일 bookmark 객체를 삭제합니다.
        """
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        단일 bookmark 객체를 삭제합니다.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)