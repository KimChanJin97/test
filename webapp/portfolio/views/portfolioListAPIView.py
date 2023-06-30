from rest_framework.generics import ListAPIView

from portfolio.serializers import PortfolioSerializer
from portfolio.models import Portfolio


class PortfolioListAPIView(ListAPIView):
    serializer_class = PortfolioSerializer
    ordering = ['id']

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Portfolio.objects.filter(user=user_id)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

