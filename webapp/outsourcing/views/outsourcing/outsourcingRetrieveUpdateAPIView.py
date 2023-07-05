from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from outsourcing.models import Outsourcing
from outsourcing.serializers import OutsourcingSerializer
from portfolio.models import Portfolio


# portfolios/ <int:portfolio_id>/outsourcings/ <int:outsourcing_id>/
# portfolio FK
class OutsourcingRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    lookup_url_kwarg = 'os_uuid'
    queryset = Outsourcing.objects.all()
    serializer_class = OutsourcingSerializer

    def get_object(self):
        user_uuid = self.request.user.uuid
        portfolio_uuid = self.kwargs['portfolio_uuid']
        outsourcing_uuid = self.kwargs['os_uuid']

        try:
            outsourcing = Outsourcing.objects.get(
                portfolio__user=user_uuid,
                portfolio=portfolio_uuid,
                uuid=outsourcing_uuid
            )
            return outsourcing
        except Outsourcing.DoesNotExist:
            return Response({"error": "외주가 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 outsourcing 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 outsourcing 객체를 수정합니다.
        """
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 outsourcing 객체를 수정합니다.
        """
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        portfolio = self.get_portfolio()
        serializer.save(portfolio=portfolio)

    def get_portfolio(self):
        user_uuid = self.request.user.uuid
        portfolio_uuid = self.kwargs['portfolio_uuid']

        portfolio = Portfolio.objects.get(
            user=user_uuid,
            uuid=portfolio_uuid
        )
        return portfolio
