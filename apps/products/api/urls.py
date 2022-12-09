from rest_framework import routers
from django.urls import path
from apps.products.api.viewset import *

router = routers.DefaultRouter()

router.register(r'category', CategoryViewSet, basename='category')  # список category
router.register(r'product', ProductViewSet, basename='transport')  # filtr по category, lt gt
router.register(r'allproduct', AllProductViewSet, basename='transport')
router.register(r'typename', TypeViewSet, basename='transport')  # filtr по type_name

urlpatterns = router.urls

urlpatterns += [
        path('transport-detail/<int:pk>', TransportDetailView.as_view()),
]
