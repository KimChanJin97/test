from rest_framework.generics import ListCreateAPIView

from work.models import Work
from work.serializers import WorkSerializer
from portfolio.models import Portfolio


class WorkListCreateAPIView(ListCreateAPIView):
    serializer_class = WorkSerializer
    ordering = ['id']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Work.objects.none()

        user_uuid = self.kwargs['user_uuid']
        portfolio_id = self.kwargs['portfolio_id']
        queryset = Work.objects.filter(
            portfolio__user__user_uuid=user_uuid,
            portfolio_id=portfolio_id
        )
        return queryset

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 모든 work 객체들을 반환합니다.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 work 객체를 생성합니다.
        """
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        portfolio = self.get_portfolio()
        serializer.save(portfolio=portfolio)

    def get_portfolio(self):
        user_uuid = self.kwargs['user_uuid']
        portfolio_id = self.kwargs['portfolio_id']

        portfolio = Portfolio.objects.get(
            user__user_uuid=user_uuid,
            id=portfolio_id
        )
        return portfolio
