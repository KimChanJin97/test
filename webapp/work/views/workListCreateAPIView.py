from rest_framework.generics import ListCreateAPIView

from portfolio.models import Portfolio
from work.models import Work
from work.serializers import WorkSerializer


class WorkListCreateAPIView(ListCreateAPIView):
    serializer_class = WorkSerializer
    ordering = ['id']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Work.objects.none()

        portfolio_id = self.kwargs['portfolio_id']
        queryset = Work.objects.filter(portfolio=portfolio_id)
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
        - form-data 로 post 요청을 보내야 합니다.
        - field 필드를 제외한 모든 필드는 Null=True 입니다.
        - image 필드는 여러 개를 보낼 수 있습니다.
        """
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        portfolio = self.get_portfolio()
        serializer.save(portfolio=portfolio)

    def get_portfolio(self):
        portfolio_id = self.kwargs['portfolio_id']
        portfolio = Portfolio.objects.get(id=portfolio_id)
        return portfolio
