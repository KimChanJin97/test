from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from outsourcing.models import Outsourcing, OutsourcingComment
from outsourcing.serializers import OutsourcingCommentSerializer


class OutsourcingCommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'outsourcing_comment_id'
    queryset = OutsourcingComment.objects.all()
    serializer_class = OutsourcingCommentSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        portfolio_id = self.kwargs['portfolio_id']
        outsourcing_id = self.kwargs['outsourcing_id']

        try:
            outsourcingComment = OutsourcingComment.objects.get(
                outsourcing__portfolio__user=user_id,
                outsourcing__portfolio=portfolio_id,
                outsourcing=outsourcing_id
            )
            return outsourcingComment
        except OutsourcingComment.DoesNotExist:
            return Response({"error": "외주가 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체의 단일 comment 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        ...
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체의 단일 comment 객체를 수정합니다.
        """
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체의 단일 comment 객체를 수정합니다.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 outsourcing 객체의 단일 comment 객체를 삭제합니다.
        """
        return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        outsourcing = self.get_outsourcing()
        serializer.save(outsourcing=outsourcing, writer=self.request.user)

    def get_outsourcing(self):
        user_id = self.kwargs['user_id']
        portfolio_id = self.kwargs['portfolio_id']
        outsourcing_id = self.kwargs['outsourcing_id']

        outsourcing = Outsourcing.objects.get(
            portfolio__user=user_id,
            portfolio=portfolio_id,
            id=outsourcing_id
        )
        return outsourcing
