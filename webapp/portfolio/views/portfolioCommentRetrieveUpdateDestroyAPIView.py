from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from portfolio.models import PortfolioComment, Portfolio
from portfolio.serializers import PortfolioCommentSerializer


# localhost:8000/portfolios/{portfolio_uuid}/portfolio_comments/{portfolio_comment_uuid}
class PortfolioCommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    pass

    lookup_url_kwarg = 'portfolio_comment_uuid'
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioCommentSerializer

    def get_object(self):
        portfolio_uuid = self.kwargs['portfolio_uuid']
        portfolio_comment_uuid = self.kwargs['portfolio_comment_uuid']

        try:
            portfolioComment = PortfolioComment.objects.get(
                portfolio=portfolio_uuid,
                uuid=portfolio_comment_uuid
            )
            return portfolioComment
        except PortfolioComment.DoesNotExist:
            return Response({"error": "외주 댓글이 존재하지 않습니다."})

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
        serializer.save(portfolio=portfolio, writer=self.request.user)

    def get_portfolio(self):
        portfolio_uuid = self.kwargs['portfolio_uuid']

        portfolio = Portfolio.objects.get(
            uuid=portfolio_uuid,
        )
        return portfolio
