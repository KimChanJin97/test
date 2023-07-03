from rest_framework.generics import ListCreateAPIView
from outsourcing.serializers import OutsourcingCommentSerializer
from outsourcing.models import OutsourcingComment, Outsourcing


class OutsourcingCommentListCreateAPIView(ListCreateAPIView):
    serializer_class = OutsourcingCommentSerializer
    ordering = ['id']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return OutsourcingComment.objects.none()

        user_id = self.kwargs['user_id']
        portfolio_id = self.kwargs['portfolio_id']
        outsourcing_id = self.kwargs['outsourcing_id']

        queryset = OutsourcingComment.objects.filter(
            outsourcing__portfolio__user=user_id,
            outsourcing__portfolio=portfolio_id,
            outsourcing=outsourcing_id
        )
        return queryset

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체의 모든 comment 객체들을 조회합니다.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체의 단일 comment 객체를 생성합니다.
        """
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        outsourcing = self.get_outsourcing()
        serializer.save(outsourcing=outsourcing, writer=self.response.user)

    def get_outsourcing(self):
        user_id = self.kwargs['user_id']
        portfolio_id = self.kwargs['portfolio_id']
        outsourcing_id = self.kwargs['outsourcing_id']

        outsourcing = Outsourcing.objects.filter(
            portfolio__user=user_id,
            portfolio=portfolio_id,
            id=outsourcing_id
        )
        return outsourcing


