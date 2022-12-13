from rest_framework import serializers
from apps.applications.models import *


class ObjectImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = ObjectImage
        fields = ['images']


class ObjectsSerializer(serializers.ModelSerializer):

    object_images = ObjectImageSerializer(many=True, read_only=True)

    class Meta:
        
        model = Objects
        fields = ['id', 'title', 'desc', 'object_images']


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ['images']


class ArticleSerializer(serializers.ModelSerializer):
    article_images = ArticleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'desc', 'article_images']


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Applications
        fields = ['name', 'number', 'email', 'sms']

