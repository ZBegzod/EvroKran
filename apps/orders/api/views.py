from rest_framework.response import Response
from rest_framework.generics import mixins, CreateAPIView
from rest_framework import status, viewsets
from .serializers import *


class OrderCreateApiView(CreateAPIView):
    serializer_class = OrderCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, owner=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderApiViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        query_set = Order.objects.filter(owner_id=self.request.user.id).first()
        return query_set
