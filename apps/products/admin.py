from django.contrib import admin
from apps.products.models import *

admin.site.register(Doc)
admin.site.register(TransportImage)
admin.site.register(TypeTransport)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('name', 'ton', 'arrow_length', 'type_transport')
