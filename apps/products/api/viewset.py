from rest_framework import generics
from rest_framework import viewsets, mixins
from apps.products.api.filters import *
from apps.products.api.serializers import *
from apps.products.models import Transport


class ProductViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    filterset_class = TransportFilter


class AllProductViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TypeViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportTypeSerializer
    filterset_class = TypeFilter


class TransportDetailView(generics.RetrieveAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportDetailSerializer
    lookup_url_kwarg = 'pk'
