from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from portfolio.models import Portfolio
from portfolio.models import PortfolioTimeline
from portfolio.serializers import PortfolioTimelineSerializer


# localhost:8000/portfolios/<int:portfolio_uuid>/portfolio_abilities/<int:portfolio_ability_uuid>/
class PortfolioTimelineRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'portfolio_timeline_uuid'
    queryset = PortfolioTimeline.objects.all()
    serializer_class = PortfolioTimelineSerializer

    def get_object(self):
        portfolio_timeline_uuid = self.kwargs['portfolio_timeline_uuid']

        try:
            portfolio_timeline = PortfolioTimeline.objects.get(
                uuid=portfolio_timeline_uuid
            )
            return portfolio_timeline
        except PortfolioTimeline.DoesNotExist:
            return Response({"error": "외주 타임라인이 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 outsourcing 객체의 단일 outsourcingComment 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        ...
        [ 설명 ]
        - 단일 portfolio 객체의 단일 outsourcing 객체의 단일 outsourcingComment 객체를 수정합니다.
        """
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 outsourcing 객체의 단일 outsourcingComment 객체를 수정합니다.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 outsourcing 객체의 단일 outsourcingComment 객체를 삭제합니다.
        """
        return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        portfolio = self.get_portfolio()
        serializer.save(portfolio=portfolio)

    def get_portfolio(self):
        portfolio_uuid = self.kwargs['portfolio_uuid']

        portfolio = Portfolio.objects.get(
            uuid=portfolio_uuid,
        )
        return portfolio
