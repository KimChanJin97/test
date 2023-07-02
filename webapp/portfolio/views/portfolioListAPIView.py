from rest_framework.generics import ListAPIView

from portfolio.serializers import PortfolioSerializer
from portfolio.models import Portfolio


# TODO: 일단 포트폴리오 객체는 하나로 고정. POST 구현 안함
class PortfolioListAPIView(ListAPIView):
    serializer_class = PortfolioSerializer
    ordering = ['id']

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Portfolio.objects.filter(
            user_id=user_id
        )
        return queryset

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 모든 portfolio 객체들을 조회합니다.
        """
        return self.list(request, *args, **kwargs)



