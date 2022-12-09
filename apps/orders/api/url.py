from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()

# router.register(r'product', ProductViewSet, basename='product')
# router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = router.urls

urlpatterns += [

    #     path('change/', change_password),
    #     path('recovery/<int:pk>/', RecoveryProfileView.as_view()),  # rezerv
]