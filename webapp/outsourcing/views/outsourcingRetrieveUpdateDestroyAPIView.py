from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from outsourcing.models import Outsourcing
from outsourcing.serializers import OutsourcingSerializer
from portfolio.models import Portfolio
from user.models import User


class OutsourcingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'outsourcing_id'
    queryset = Outsourcing.objects.all()
    serializer_class = OutsourcingSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "유저가 존재하지 않습니다."})

        portfolio_id = self.kwargs['portfolio_id']
        try:
            portfolio = Portfolio.objects.get(id=portfolio_id)
        except Portfolio.DoesNotExist:
            return Response({"error": "포트폴리오가 존재하지 않습니다."})

        outsourcing_id = self.kwargs['outsourcing_id']
        try:
            return Outsourcing.objects.get(id=outsourcing_id, user=user, portfolio=portfolio)
        except Outsourcing.DoesNotExist:
            return Response({"error": "외주가 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체를 반환합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체를 수정합니다.
        """
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체를 수정합니다.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체를 삭제합니다.
        """
        return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        user = self.get_user()
        portfolio = self.get_portfolio()
        serializer.save(user=user, portfolio=portfolio)

    def get_user(self):
        user_id = self.kwargs['user_id']
        user = User.objects.get(id=user_id)
        return user

    def get_portfolio(self):
        portfolio_id = self.kwargs['portfolio_id']
        user = self.get_user()
        portfolio = Portfolio.objects.get(id=portfolio_id, user=user)
        return portfolio
