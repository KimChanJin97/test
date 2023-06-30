from rest_framework.decorators import api_view
from rest_framework.response import Response

from work.models import Work
from work.serializers import WorkSerializer


@api_view(['GET'])
def allWorks(request):
    allworks = Work.objects.all()
    serializer = WorkSerializer(allworks, many=True)
    return Response(serializer.data)
