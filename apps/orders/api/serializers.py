from rest_framework import serializers
from apps.order.models import *

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        