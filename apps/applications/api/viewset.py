from rest_framework import viewsets, mixins
from apps.applications.api.serializers import ObjectsSerializer
from apps.applications.models import *


class ObjectsViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Objects.objects.all()
    serializer_class = ObjectsSerializer
