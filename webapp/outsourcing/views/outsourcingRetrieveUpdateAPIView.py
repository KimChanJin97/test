from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from outsourcing.models import Outsourcing
from outsourcing.serializers import OutsourcingSerializer
from portfolio.models import Portfolio
from user.models import User


class OutsourcingRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    lookup_url_kwarg = 'outsourcing_id'
    queryset = Outsourcing.objects.all()
    serializer_class = OutsourcingSerializer

    def get_object(self):
        user_uuid = self.kwargs['user_uuid']
        portfolio_id = self.kwargs['portfolio_id']
        outsourcing_id = self.kwargs['outsourcing_id']

        try:
            outsourcing = Outsourcing.objects.get(
                portfolio__user__user_uuid=user_uuid,
                portfolio_id=portfolio_id,
                id=outsourcing_id
            )
            return outsourcing
        except outsourcing.DoesNotExist:
            return Response({"error": "외주가 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체를 수정합니다.
        """
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체를 수정합니다.
        """
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
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
