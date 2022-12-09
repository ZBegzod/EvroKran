from django.db import models

# Create your models here.


class Doc(models.Model):
    document = models.FileField(null=True)


class Category(models.Model):
    image = models.ImageField(upload_to='category/images', null=True)
    title = models.CharField(max_length=100, null=False, default='')

    def __str__(self):
        return self.title


class TypeTransport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transport(models.Model):
    type_transport = models.ForeignKey(TypeTransport, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, default='', null=False, blank=True)
    ton = models.DecimalField(max_digits=5, decimal_places=2)
    arrow_length = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    document = models.ForeignKey(Doc, on_delete=models.CASCADE, null=True)
    characteristics = models.TextField(default='')
    mobile_cranes = 'mc'
    crawler_cranes = 'cc'
    lowbed_trawls = 'lt'
    modular_platforms = 'mp'
    Select_type = [
        (mobile_cranes, 'mobile_cranes'),
        (crawler_cranes, 'crawler_cranes'),
        (lowbed_trawls, 'lowbed_trawls'),
        (modular_platforms, 'modular_platforms'),
    ]
    select_type = models.CharField(
        max_length=2,
        choices=Select_type,
        default=mobile_cranes,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}"


class TransportImage(models.Model):
    images = models.ImageField(upload_to='transport/images', null=True)
    transport = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True, related_name='transport_images')

    def __str__(self) -> str:
        return f"{self.transport}"
