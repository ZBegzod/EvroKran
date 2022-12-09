from rest_framework import routers
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from apps.applications.api.viewset import *

router = routers.DefaultRouter()
router.register(r'objects', ObjectsViewSet, basename='object')

urlpatterns = [

        path('objects-list/', ObjectListView.as_view()),
        path('object-detail/<int:pk>/', ObjectDetailView.as_view()), 
        path('create-appv2/', CreateContact.as_view()), 
        # path('create-contact/', create_app), 

]       


# urlpatterns = format_suffix_patterns(urlpatterns)
