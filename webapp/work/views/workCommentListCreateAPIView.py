from rest_framework.generics import ListCreateAPIView

from work.models import WorkComment, Work
from work.serializers import WorkCommentSerializer


# portfolios/{portfolio_id}/works/{work_id}/work_comments/
# work FK
# writer FK
class WorkCommentListCreateAPIView(ListCreateAPIView):
    serializer_class = WorkCommentSerializer
    ordering = ['id']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return WorkComment.objects.none()

        user_id = self.request.user.id
        portfolio_id = self.kwargs['portfolio_id']
        work_id = self.kwargs['work_id']

        queryset = WorkComment.objects.filter(
            work__portfolio__user=user_id,
            work__portfolio=portfolio_id,
            work=work_id
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
        user_id = self.request.user.id
        portfolio_id = self.kwargs['portfolio_id']
        work_id = self.kwargs['work_id']

        work = Work.objects.get(
            work__user=user_id,
            work=portfolio_id,
            id=work_id
        )
        return work
