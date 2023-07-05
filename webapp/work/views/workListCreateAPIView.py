from rest_framework.generics import ListCreateAPIView

from work.models import Work
from work.serializers import WorkSerializer
from portfolio.models import Portfolio
from rest_framework.response import Response

# localhost:8000/portfolios/{portfolio_id}/works
# portfolio <FK>
# field
# description
class WorkListCreateAPIView(ListCreateAPIView):
    serializer_class = WorkSerializer
    ordering = ['created_at']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Work.objects.none()

        portfolio_uuid = self.kwargs['portfolio_uuid']
        try:
            queryset = Work.objects.filter(
                portfolio=portfolio_uuid
            )
            return queryset
        except Work.DoesNotExist:
            return Response({"error": "작업물이 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 모든 work 객체들을 조회합니다.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 work 객체를 생성합니다.
        """
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        portfolio = self.get_portfolio()
        serializer.save(portfolio=portfolio)

    def get_portfolio(self):
        portfolio_uuid = self.kwargs['portfolio_uuid']

        try:
            portfolio = Portfolio.objects.get(
                uuid=portfolio_uuid
            )
            return portfolio
        except Portfolio.DoesNotExist:
            return Response({"error": "포트폴리오가 존재하지 않습니다."})
