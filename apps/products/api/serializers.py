from rest_framework import serializers
from apps.products.models import *


class TransportImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransportImage
        fields = '__all__'


class TransportCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'image']


class TransportDocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = ['document']


class TransportDetailSerializer(serializers.ModelSerializer):
    transport_images = TransportImageSerializers(many=True, read_only=True)
    category = TransportCategorySerializers(read_only=True)
    document = TransportDocumentSerializers(read_only=True)

    class Meta:
        model = Transport
        fields = ['id',
                  'name',
                  'ton',
                  'arrow_length',
                  'description',
                  'category',
                  'document',
                  'transport_images',
                  'characteristics']


class TransportSerializer(serializers.ModelSerializer):
    transport_images = TransportImageSerializers(many=True)
    type_transport = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Transport
        fields = ["id", "name", "ton",
                  "arrow_length",
                  "description",
                  "document",
                  "characteristics",
                  "transport_images",
                  "type_transport",
                  "category"]


class CategorySerializer(serializers.ModelSerializer):
    transport_category = TransportSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "title", 'image', 'transport_category']


class TransportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ('id', 'type_transport', 'name', 'ton')
