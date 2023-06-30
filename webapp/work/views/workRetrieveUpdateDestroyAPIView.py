from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from portfolio.models import Portfolio
from work.models import Work
from work.serializers import WorkSerializer


class WorkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'work_id'
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    def get_object(self):
        work_id = self.kwargs['work_id']
        try:
            return Work.objects.get(pk=work_id)
        except Work.DoesNotExist:
            return Response({"error": "작업물이 존재하지 않습니다."})

    def get(self, request, *args, **kwargs):
        """
        ...
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 work 객체를 반환합니다.
        """
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        """
        ...
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 work 객체를 수정합니다.
        - form-data 로 patch 요청을 보내야 합니다.
        - field 필드를 제외한 모든 필드는 Null=True 입니다.
        - image 필드는 여러 개를 보낼 수 있습니다.
        """
        return self.partial_update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - 단일 user 객체의 단일 portfolio 객체의 단일 work 객체를 수정합니다.
        - form-data 로 patch 요청을 보내야 합니다.
        - field 필드를 제외한 모든 필드는 Null=True 입니다.
        - image 필드는 여러 개를 보낼 수 있습니다.
        """
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Extract the portfolio ID from the URL
        portfolio_id = self.kwargs.get('portfolio_id')

        # Get the portfolio object
        try:
            portfolio = Portfolio.objects.get(id=portfolio_id)
        except Portfolio.DoesNotExist:
            return Response({"error": "존재하지 않는 포트폴리오입니다."}, status=status.HTTP_400_BAD_REQUEST)

        # Assign the portfolio object to the 'portfolio' field of the work object
        request.data['portfolio'] = portfolio.id

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        # Retrieve the updated instance to include the images
        updated_instance = self.get_object()
        updated_serializer = self.get_serializer(updated_instance)
        return Response(updated_serializer.data)

    def delete(self, request, *args, **kwargs):
        """
        [ 설명 ]
        - localhost:8000/users/{user_id}/portfolios/{portfolio_id}/works/{work_id}
        - 단일 user 객체의 단일 portfolio 객체의 단일 work 객체를 삭제합니다.
        """
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
