from rest_framework.generics import ListAPIView
from bookmark.models import Bookmark
from bookmark.serializers import BookmarkSerializer
from rest_framework.response import Response


# localhost:8000/bookmarks/ rootBookmarkListAPIView
# adder
# work
class RootBookmarkListAPIView(ListAPIView):
    serializer_class = BookmarkSerializer
    ordering = ['id']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Bookmark.objects.none()

        try:
            adder = self.request.user.id
            queryset = Bookmark.objects.filter(
                adder=adder,
            ).order_by('id')
            return queryset
        except Bookmark.DoesNotExist:
            return Response({"error": "북마크가 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        root 페이지의 bookmark 페이지에서 사용됩니다.
        단일 user 객체의 모든 bookmark 객체들을 조회합니다.
        """
        return self.list(request, *args, **kwargs)