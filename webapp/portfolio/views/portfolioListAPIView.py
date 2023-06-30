from rest_framework.generics import ListAPIView

from portfolio.serializers import PortfolioSerializer
from portfolio.models import Portfolio


class PortfolioListAPIView(ListAPIView):
    serializer_class = PortfolioSerializer
    ordering = ['id']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Portfolio.objects.none()
        user_id = self.kwargs['user_id']
        queryset = Portfolio.objects.filter(user=user_id)
        return queryset

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 모든 portfolio 객체들을 조회합니다.
        - 현재는 portfolio 템플릿을 하나로만 운용하므로 하나만 조회됩니다.
        - 때문에 post 요청은 일부로 만들지 않았습니다. 오로지 get, put, update 요청만 가능합니다.
        """
        return self.list(request, *args, **kwargs)

