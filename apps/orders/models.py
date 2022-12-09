from django.db import models
# Create your models here.


class Order(models.Model):

    name = models.CharField(max_length=100, default='')
    number = models.CharField(max_length=50, default='')
    email = models.EmailField(null=True, blank=True)
    sms = models.CharField(max_length=120, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

