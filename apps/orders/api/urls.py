from rest_framework import routers
from django.urls import path
from .views import OrderApiViewSet, OrderCreateApiView

router = routers.DefaultRouter()

router.register(r'orders', OrderApiViewSet, basename='order')
# router.register(r'order-create', OrderCreateApiView, basename='order-create')

urlpatterns = router.urls

urlpatterns += [

    path('order-create', OrderCreateApiView.as_view(), name='create-order'),

]
