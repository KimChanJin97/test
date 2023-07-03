from rest_framework.generics import ListAPIView
from work.serializers import WorkSerializer
from work.models import Work


# localhost:8000/works
# portfolio <FK>
# field
# description
class RootWorkListAPIView(ListAPIView):
    serializer_class = WorkSerializer
    ordering = ['id']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Work.objects.none()

        queryset = Work.objects.all().order_by('id')
        return queryset

    def get(self, request, *args, **kwargs):
        """
        단일 유저 객체의 모든 북마크 객체들을 조회합니다.
        """
        return self.list(request, *args, **kwargs)