from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from .serializers import *


@api_view(["GET", "POST"])
@csrf_exempt
def create_order(request):
    if request.method == 'GET':

        serializer = OrderCreateSerializer()

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = OrderCreateSerializer(data=request.data, owner=request.user)

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
