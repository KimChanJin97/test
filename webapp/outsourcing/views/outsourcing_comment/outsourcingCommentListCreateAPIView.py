from rest_framework.generics import ListCreateAPIView
from outsourcing.serializers import OutsourcingCommentSerializer
from outsourcing.models import OutsourcingComment, Outsourcing


# portfolios/{portfolio_id}/outsourcings/{outsourcing_id}/outsourcing_comments/
# outsourcing FK
# writer FK
class OutsourcingCommentListCreateAPIView(ListCreateAPIView):
    serializer_class = OutsourcingCommentSerializer
    ordering = ['created_at']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return OutsourcingComment.objects.none()

        portfolio_uuid = self.kwargs['portfolio_uuid']
        outsourcing_uuid = self.kwargs['os_uuid']

        queryset = OutsourcingComment.objects.filter(
            outsourcing__portfolio=portfolio_uuid,
            outsourcing=outsourcing_uuid
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
        outsourcing = self.get_outsourcing()
        serializer.save(outsourcing=outsourcing, writer=self.request.user)

    def get_outsourcing(self):
        portfolio_uuid = self.kwargs['portfolio_uuid']
        outsourcing_uuid = self.kwargs['os_uuid']

        outsourcing = Outsourcing.objects.get(
            portfolio=portfolio_uuid,
            uuid=outsourcing_uuid
        )
        return outsourcing


