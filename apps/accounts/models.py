from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    phone_number = models.CharField(max_length=90, unique=True)
    USERNAME_FIELD = 'phone_number'
    objects = CustomUserManager()

    @property
    def get_user_token(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data

    def __str__(self):
        return self.phone_number

