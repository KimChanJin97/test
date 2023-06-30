from rest_framework.generics import ListCreateAPIView

from work.serializers import WorkSerializer
from portfolio.models import Portfolio
from work.models import Work

class WorkListCreateAPIView(ListCreateAPIView):
    serializer_class = WorkSerializer
    ordering = ['id']

    def get_queryset(self):
        portfolio_id = self.kwargs['portfolio_id']
        queryset = Work.objects.filter(portfolio=portfolio_id)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        portfolio = self.get_portfolio()
        serializer.save(portfolio=portfolio)

    def get_portfolio(self):
        portfolio_id = self.kwargs['portfolio_id']
        portfolio = Portfolio.objects.get(id=portfolio_id)
        return portfolio



