from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from portfolio.models import Portfolio
from portfolio.serializers import PortfolioSerializer


class PortfolioRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    lookup_url_kwarg = 'portfolio_id'
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    parser_classes = [MultiPartParser, FormParser]


    def get_object(self):
        portfolio_id = self.kwargs['portfolio_id']
        try:
            return Portfolio.objects.get(pk=portfolio_id)
        except Portfolio.DoesNotExist:
            return Response({"error": "존재하지 않는 포트폴리오입니다."})

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

