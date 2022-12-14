from rest_framework import serializers
from apps.accounts.models import CustomUser
from apps.orders.models import *
from apps.products.models import *


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    transport_images = ProductImageSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    type_transport = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Transport
        fields = [
            'type_transport', 'transport_images',
            'name', 'ton', 'arrow_length', 'description',
            'category', 'document', 'characteristics',
            'select_type'

        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name',
            'email', 'phone_number',
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'product', 'name', 'number',
            'email', 'owner'
        ]


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    owner = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            'owner', 'product',
            'name', 'number',
            'email', 'sms'
        ]
