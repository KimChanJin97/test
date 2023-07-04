from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from work.models import Work, WorkComment
from work.serializers import WorkCommentSerializer


# portfolios/{portfolio_id}/works/{work_id}/work_comments/{work_comment_id}
# work FK
# writer FK
class WorkCommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'work_comment_id'
    queryset = Work.objects.all()
    serializer_class = WorkCommentSerializer

    def get_object(self):
        user_id = self.request.user.id
        portfolio_id = self.kwargs['portfolio_id']
        work_id = self.kwargs['work_id']
        work_comment_id = self.kwargs['work_comment_id']

        try:
            workComment = WorkComment.objects.get(
                work__portfolio__user=user_id,
                work__portfolio=portfolio_id,
                work=work_id,
                id=work_comment_id
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
        user_id = self.request.user.id
        portfolio_id = self.kwargs['portfolio_id']
        work_id = self.kwargs['work_id']

        work = Work.objects.get(
            portfolio__user=user_id,
            portfolio=portfolio_id,
            id=work_id
        )
        return work
