from rest_framework import routers
from django.urls import path
from .views import OrderApiViewSet, create_order

router = routers.DefaultRouter()

router.register(r'orders', OrderApiViewSet, basename='order')

urlpatterns = router.urls

urlpatterns += [

    path('', create_order, name='create-order'),

]
