from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError(_('The phone number must be enter'))

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Super user must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Super user must have is_superuser=True'))
        return self.create_user(phone_number, password, **extra_fields)
