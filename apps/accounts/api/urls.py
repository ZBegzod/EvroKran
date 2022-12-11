from django.urls import path

from .views import (
    RegisterAPIView,
    LoginAPIView,
    ResetPasswordRequestEmailAPIView,
    PasswordTokenCheckAPI,
    SetPasswordAPIView
)

urlpatterns = [

    path('user-register', RegisterAPIView.as_view(), name='user-register'),
    path('user-login', LoginAPIView.as_view(), name='user-login'),
    path('reset-password', ResetPasswordRequestEmailAPIView.as_view(), name='reset-password'),
    path('password-token-check/<uidb64>/<token>', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('set-password', SetPasswordAPIView.as_view(), name='set-password'),

]
