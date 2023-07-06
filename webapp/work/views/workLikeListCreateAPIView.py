from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from work.models import WorkLike, Work
from work.serializers import WorkLikeSerializer


class WorkLikeListCreateAPIView(ListCreateAPIView):
    serializer_class = WorkLikeSerializer
    ordering = ['created_at']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return WorkLike.objects.none()

        work_uuid = self.kwargs['work_uuid']
        queryset = WorkLike.objects.filter(work=work_uuid)
        return queryset

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 work 객체의 모든 worklike 객체들을 조회합니다.
        - root 페이지에서 단일 work 객체의 모든 worklike 객체들을 조회합니다.
        """
        work_uuid = self.kwargs['work_uuid']
        like_counts = WorkLike.objects.filter(work=work_uuid).count()
        return Response({"like_counts": like_counts})

    def post(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 work 객체의 단일 worklike 객체를 생성합니다.
        - root 페이지에서 단일 work 객체의 단일 worklike 객체를 생성합니다.
        """
        liker = self.request.user
        work = self.get_work()
        liked_work = WorkLike.objects.filter(liker=liker, work=work).first()

        if liked_work:
            liked_work.delete()
            return Response({"message": "좋아요를 취소합니다."})
        else:
            WorkLike.objects.create(liker=liker, work=work)
            return Response({"message": "좋아요를 누릅니다."})

    def perform_create(self, serializer):
        work = self.get_work()
        serializer.save(work=work, liker=self.request.user)

    def get_work(self):
        work_uuid = self.kwargs['work_uuid']
        work = Work.objects.get(uuid=work_uuid)
        return work
