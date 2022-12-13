from django.urls import path
from .views import *
from rest_framework import routers
from apps.applications.api.viewset import *

router = routers.DefaultRouter()
router.register(r'objects', ObjectsViewSet, basename='object')
router.register(r'article', ArticleViewSet, basename='article')

urlpatterns = router.urls

urlpatterns += [

        path('create-app/', CreateContact.as_view()),

]

