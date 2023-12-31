from rest_framework.generics import ListAPIView
from work.serializers import RootWorkSerializer
from work.models import Work
import django_filters
from core.choices import INTERESTS
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from config.pagination import DefaultPagination


class WorkFilter(django_filters.FilterSet):
    field = django_filters.MultipleChoiceFilter(choices=INTERESTS)

    class Meta:
        model = Work
        fields = ['field']


# localhost:8000/works
# portfolio <FK>
# field
# description
class RootWorkListAPIView(ListAPIView):
    serializer_class = RootWorkSerializer
    ordering = ['created_at']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = WorkFilter
    search_fields = ['description']
    pagination_class = DefaultPagination


    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Work.objects.none()

        queryset = Work.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        """
        단일 유저 객체의 모든 북마크 객체들을 조회합니다.
        """
        return self.list(request, *args, **kwargs)