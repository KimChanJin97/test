from rest_framework.generics import ListCreateAPIView
from portfolio.serializers import PortfolioCommentSerializer
from portfolio.models import PortfolioComment, Portfolio


# localhost:8000/portfolios/{portfolio_uuid}/portfolio_comments/
class PortfolioCommentListCreateAPIView(ListCreateAPIView):

    serializer_class = PortfolioCommentSerializer
    ordering = ['created_at']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return PortfolioComment.objects.none()

        portfolio_uuid = self.kwargs['portfolio_uuid']

        queryset = PortfolioComment.objects.filter(
            portfolio=portfolio_uuid,
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
        portfolio = self.get_portfolio()
        serializer.save(portfolio=portfolio, writer=self.request.user)

    def get_portfolio(self):
        portfolio_uuid = self.kwargs['portfolio_uuid']

        portfolio = Portfolio.objects.get(
            uuid=portfolio_uuid,
        )
        return portfolio

