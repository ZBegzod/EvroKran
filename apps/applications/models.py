from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Applications(models.Model):
    name = models.CharField(max_length=120)
    number = models.CharField(max_length=120)
    email = models.EmailField(null=True)
    sms = models.TextField(max_length=150, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Objects(models.Model):
    title = models.CharField(max_length=150)
    desc = RichTextField(null=True)

    def __str__(self) -> str:
        return f"{self.title}"


class ObjectImage(models.Model):
    images = models.ImageField(upload_to='object/images')
    object = models.ForeignKey(Objects, on_delete=models.SET_NULL, null=True, related_name='object_images')

    def __str__(self) -> str:
        return f"{self.object}"


class Article(models.Model):
    title = models.CharField(max_length=150)
    desc = RichTextField(null=True)

    def __str__(self) -> str:
        return f"{self.title}"


class ArticleImage(models.Model):
    images = models.ImageField(upload_to='article/images')
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='article_images')

    def __str__(self) -> str:
        return f"{self.article}"
