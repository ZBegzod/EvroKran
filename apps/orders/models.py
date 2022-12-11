from django.db import models
from apps.products.models import Transport
from django.conf import settings
# Create your models here.


class Order(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Transport, on_delete=models.SET_NULL,
                                null=True, blank=True)
    name = models.CharField(max_length=100, default='')
    number = models.CharField(max_length=50, default='')
    email = models.EmailField(null=True, blank=True)
    sms = models.CharField(max_length=120, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

