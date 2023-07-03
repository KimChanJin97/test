from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from outsourcing.models import Outsourcing
from outsourcing.serializers import OutsourcingSerializer
from portfolio.models import Portfolio



# portfolios/ <int:portfolio_id>/outsourcings/
# portfolio FK
class OutsourcingListCreateAPIView(ListCreateAPIView):
    serializer_class = OutsourcingSerializer
    ordering = ['id']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Outsourcing.objects.none()

        user_id = self.request.user.id
        portfolio_id = self.kwargs['portfolio_id']

        queryset = Outsourcing.objects.filter(
            portfolio__user=user_id,
            portfolio=portfolio_id
        )
        return queryset

    def get(self, request, *args, **kwargs):
        """
        단일 user 객체의 단일 portfolio 객체의 모든 outsourcing 객체들을 조회합니다.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        outsourcing_exists = self.check_outsourcing_exists()
        if outsourcing_exists:
            return Response({"error": "외주는 1개만 생성하여 관리해야 합니다."})
        """
        단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체를 생성합니다.
        만약 외주 객체 1개가 존재할 때 post 요청을 할 경우 예외를 발생시킵니다.
        """
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        portfolio = self.get_portfolio()
        serializer.save(portfolio=portfolio)

    def get_portfolio(self):
        # user_id = self.kwargs['user_id']
        user_id = self.request.user.id
        portfolio_id = self.kwargs['portfolio_id']

        portfolio = Portfolio.objects.get(
            user=user_id,
            id=portfolio_id
        )
        return portfolio

    def check_outsourcing_exists(self):
        # user_id = self.kwargs['user_id']
        user_id = self.request.user.id
        portfolio_id = self.kwargs['portfolio_id']

        exists = Outsourcing.objects.filter(
            portfolio__user=user_id,
            portfolio=portfolio_id
        ).exists()

        return exists
