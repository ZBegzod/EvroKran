from rest_framework import viewsets, mixins
from apps.applications.models import *
from apps.applications.api.serializers import (
    ObjectsSerializer, ArticleSerializer
)


class ObjectsViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Objects.objects.all()
    serializer_class = ObjectsSerializer


class ArticleViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
