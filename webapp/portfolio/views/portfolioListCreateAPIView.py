from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from portfolio.serializers import PortfolioSerializer
from portfolio.models import Portfolio


# TODO: 일단 포트폴리오 객체는 하나로 고정. POST 구현 안함
class PortfolioListCreateAPIView(ListCreateAPIView):
    serializer_class = PortfolioSerializer
    ordering = ['id']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Portfolio.objects.none() # 수정

        # user_id = self.kwargs['user_id']
        user_id = self.request.user.id
        queryset = Portfolio.objects.filter(
            user=user_id
        )
        return queryset

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 모든 portfolio 객체들을 조회합니다.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        portfolio_exists = self.check_portfolio_exists()
        if portfolio_exists:
            return Response({"error": "현재 버전에서는 포트폴리오 하나만 생성할 수 있습니다."})
        """
        [ 설명 ]
        - 단일 portfolio 객체를 생성합니다.
        - 만약 portfolio 객체 1개가 존재할 때 post 요청을 할 경우 예외를 발생시킵니다.
        """
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def check_portfolio_exists(self):
        exists = Portfolio.objects.filter(
            user=self.request.user.id
        ).exists()

        return exists





