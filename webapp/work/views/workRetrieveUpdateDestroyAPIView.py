from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from work.models import Work
from work.serializers import WorkSerializer
from portfolio.models import Portfolio


# localhost:8000/portfolios/{portfolio_id}/works/{work_id}
# portfolio <FK>
# field
# description
class WorkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'work_id'
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    def get_object(self):
        user_id = self.request.user.id
        portfolio_id = self.kwargs['portfolio_id']
        work_id = self.kwargs['work_id']

        try:
            work = Work.objects.get(
                portfolio__user=user_id,
                portfolio=portfolio_id,
                id=work_id
            )
            return work
        except Work.DoesNotExist:
            return Response({"error": "작업물이 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 work 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        ...
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 work 객체를 수정합니다.
        """
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 work 객체를 수정합니다.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 work 객체를 삭제합니다.
        """
        return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        portfolio = self.get_portfolio()
        serializer.save(portfolio=portfolio)

    def get_portfolio(self):
        # user_id = self.kwargs['user_id']
        user_id = self.request.user.id
        portfolio_id = self.kwargs['portfolio_id']

        try:
            portfolio = Portfolio.objects.get(
                user=user_id,
                id=portfolio_id
            )
            return portfolio
        except Portfolio.DoesNotExist:
            return Response({"error": "포트폴리오가 존재하지 않습니다."})
