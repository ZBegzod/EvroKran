from django.contrib import admin

# Register your models here.
from apps.applications.models import *

admin.site.register(Applications)
admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(Objects)
admin.site.register(ObjectImage)

