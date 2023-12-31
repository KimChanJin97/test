from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from outsourcing.models import Outsourcing, OutsourcingComment
from outsourcing.serializers import OutsourcingCommentSerializer


# portfolios/{portfolio_id}/outsourcings/{outsourcing_id}/outsourcing_comments/{outsourcing_comment_id}
# outsourcing FK
# writer FK
class OutsourcingCommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'osc_uuid'
    queryset = Outsourcing.objects.all()
    serializer_class = OutsourcingCommentSerializer

    def get_object(self):
        portfolio_uuid = self.kwargs['portfolio_uuid']
        outsourcing_uuid = self.kwargs['os_uuid']
        outsourcing_comment_uuid = self.kwargs['osc_uuid']

        try:
            outsourcingComment = OutsourcingComment.objects.get(
                outsourcing__portfolio=portfolio_uuid,
                outsourcing=outsourcing_uuid,
                uuid=outsourcing_comment_uuid
            )
            return outsourcingComment
        except OutsourcingComment.DoesNotExist:
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
        outsourcing = self.get_outsourcing()
        serializer.save(outsourcing=outsourcing, writer=self.request.user)

    def get_outsourcing(self):
        portfolio_uuid = self.kwargs['portfolio_uuid']
        outsourcing_uuid = self.kwargs['os_uuid']

        outsourcing = Outsourcing.objects.get(
            portfolio=portfolio_uuid,
            uuid=outsourcing_uuid
        )
        return outsourcing
