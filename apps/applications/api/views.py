from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from apps.applications.models import (
    Objects, Applications
)
from .serializers import (
    ObjectsSerializer, ApplicationSerializer,

)
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    CreateAPIView
)


class ObjectListView(ListAPIView):
    queryset = Objects.objects.all()
    serializer_class = ObjectsSerializer


class ObjectDetailView(RetrieveAPIView):
    queryset = Objects.objects.all()
    serializer_class = ObjectsSerializer
    lookup_url_kwarg = 'pk'


@api_view(["GET", "POST"])
@csrf_exempt
def create_app(request):
    if request.method == 'GET':

        serializer = ApplicationSerializer()

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = ApplicationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateContact(CreateAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationSerializer


