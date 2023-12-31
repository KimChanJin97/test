from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from portfolio.models import Portfolio
from portfolio.serializers import PortfolioSerializer
from user.models import User


# /portfolios/{portfolio_uuid}
# user <FK>
class PortfolioRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    lookup_url_kwarg = 'portfolio_uuid'
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def get_object(self):
        user_uuid = self.request.user.uuid
        portfolio_uuid = self.kwargs['portfolio_uuid']

        try:
            portfolio = Portfolio.objects.get(
                user=user_uuid,
                uuid=portfolio_uuid)
            return portfolio
        except Portfolio.DoesNotExist:
            return Response({"error": "존재하지 않는 포트폴리오입니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체를 수정합니다.
        """
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체를 수정합니다.
        """
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        user = User.objects.get(
            uuid=self.request.user.uuid
        )
        serializer.save(user=user)

