from rest_framework import serializers

from apps.products.models import *


class TransportImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransportImage
        fields = ['images']


class TransportCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'image']


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
        fields = ['name',
                  'ton',
                  'arrow_length',
                  'description',
                  'category',
                  'document',
                  'transport_images',
                  'characteristics']


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TransportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ('type_transport', 'name', 'ton')
