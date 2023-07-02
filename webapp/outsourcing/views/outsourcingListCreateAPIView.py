from rest_framework.generics import ListCreateAPIView

from outsourcing.serializers import OutsourcingSerializer
from outsourcing.models import Outsourcing
from portfolio.models import Portfolio
from user.models import User


class OutsourcingListCreateAPIView(ListCreateAPIView):
    serializer_class = OutsourcingSerializer
    ordering = ['id']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Outsourcing.objects.none()
        portfolio_id = self.kwargs['portfolio_id']
        queryset = Outsourcing.objects.filter(portfolio_id=portfolio_id).order_by('id')

        return queryset

    def get(self, request, *args, **kwargs):
        """
        단일 user 객체의 단일 portfolio 객체의 모든 outsourcing 객체들을 조회합니다.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체를 생성합니다.
        """
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        portfolio = self.get_portfolio
        user = self.get_user()
        serializer.save(user=user, portfolio=portfolio)

    def get_portfolio(self):
        portfolio_id = self.kwargs['portfolio_id']
        portfolio = Portfolio.objects.get(id=portfolio_id)
        return portfolio

    def get_user(self):
        user_id = self.kwargs['user']
        user = User.objects.get(id=user_id)
        return user
