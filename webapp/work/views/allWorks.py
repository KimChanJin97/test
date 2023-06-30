from rest_framework.decorators import api_view
from rest_framework.response import Response

from work.models import Work
from work.serializers import WorkSerializer


@api_view(['GET'])
def allWorks(request):
    """
    [ 설명 ]
    - root 페이지에서 모든 work 객체들을 조회할 때 사용할 것입니다.
    - 임시로 url을 위와 같이 설정했습니다.
    """
    allworks = Work.objects.all()
    serializer = WorkSerializer(allworks, many=True)
    return Response(serializer.data)
