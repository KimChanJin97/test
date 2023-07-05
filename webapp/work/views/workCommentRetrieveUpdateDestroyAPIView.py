from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from work.models import Work, WorkComment
from work.serializers import WorkCommentSerializer


# portfolios/{portfolio_uuid}/works/{work_uuid}/work_comments/{work_comment_uuid}
# work FK
# writer FK
class WorkCommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'work_comment_uuid'
    queryset = Work.objects.all()
    serializer_class = WorkCommentSerializer

    def get_object(self):
        portfolio_uuid = self.kwargs['portfolio_uuid']
        work_uuid = self.kwargs['work_uuid']
        work_comment_uuid = self.kwargs['work_comment_uuid']

        try:
            workComment = WorkComment.objects.get(
                work__portfolio=portfolio_uuid,
                work=work_uuid,
                uuid=work_comment_uuid
            )
            return workComment
        except WorkComment.DoesNotExist:
            return Response({"error": "작업물 댓글이 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 work 객체의 단일 workComment 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        ...
        [ 설명 ]
        - 단일 portfolio 객체의 단일 work 객체의 단일 workComment 객체를 수정합니다.
        """
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 work 객체의 단일 workComment 객체를 수정합니다.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 portfolio 객체의 단일 work 객체의 단일 workComment 객체를 삭제합니다.
        """
        return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        work = self.get_work()
        serializer.save(work=work, writer=self.request.user)

    def get_work(self):
        portfolio_uuid = self.kwargs['portfolio_uuid']
        work_uuid = self.kwargs['work_uuid']

        work = Work.objects.get(
            portfolio=portfolio_uuid,
            uuid=work_uuid
        )
        return work
