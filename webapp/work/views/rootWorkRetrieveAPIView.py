from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from work.models import Work
from work.serializers import WorkSerializer

# localhost:8000/works/{work_uuid}
# portfolio <FK>
# field
# description
class RootWorkRetrieveAPIView(RetrieveAPIView):
    lookup_url_kwarg = "work_uuid"
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    def get_object(self):
        work_uuid = self.kwargs['work_uuid']

        try:
            work = Work.objects.get(
                uuid=work_uuid,
            )
            return work
        except Work.DoesNotExist:
            return Response({"error": "작업물이 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 work 객체를 조회합니다.
        """
        return self.retrieve(request, *args, **kwargs)

