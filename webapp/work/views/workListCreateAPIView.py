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
    ordering = ['id']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Work.objects.none()

        # user_id = self.kwargs['user_id']
        user_id = self.request.user.id
        portfolio_id = self.kwargs['portfolio_id']
        try:
            queryset = Work.objects.filter(
                portfolio__user=user_id,
                portfolio=portfolio_id
            ).order_by('id')
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
        # user_id = self.kwargs['user_id']
        user_id = self.request.user.id
        portfolio_id = self.kwargs['portfolio_id']

        try:
            portfolio = Portfolio.objects.get(
                user=user_id,
                id=portfolio_id
            )
            return portfolio
        except Portfolio.DoesNotExist:
            return Response({"error": "포트폴리오가 존재하지 않습니다."})
