from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


@api_view(["GET", "POST"])
@csrf_exempt
def create_order(request):

    if request.method == 'GET':
        
        serializer = OrderSerializer()

        return Response(serializer.data)
       
    elif request.method == 'POST':

        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
