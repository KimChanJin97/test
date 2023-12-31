from rest_framework.generics import ListCreateAPIView

from work.models import WorkComment, Work
from work.serializers import WorkCommentSerializer


# portfolios/{portfolio_uuid}/works/{work_uuid}/work_comments/
# work FK
# writer FK
class WorkCommentListCreateAPIView(ListCreateAPIView):
    serializer_class = WorkCommentSerializer
    ordering = ['created_at']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return WorkComment.objects.none()

        portfolio_uuid = self.kwargs['portfolio_uuid']
        work_uuid = self.kwargs['work_uuid']

        queryset = WorkComment.objects.filter(
            work__portfolio=portfolio_uuid,
            work=work_uuid
        )
        return queryset

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 outsourcing 객체의 모든 outsourcingComment 객체들을 조회합니다.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 outsourcing 객체의 단일 outsourcingComment 객체를 생성합니다.
        """
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        work = self.get_work()
        serializer.save(work=work, writer=self.request.user)

    def get_work(self):
        portfolio_uuid = self.kwargs['portfolio_uuid']
        work_uuid = self.kwargs['work_uuid']

        work = Work.objects.get(
            portfolio=portfolio_uuid,
            uuid=work_uuid
        )
        return work
