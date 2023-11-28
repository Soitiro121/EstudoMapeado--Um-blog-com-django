from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

# Fazendo a mudança do nome na pagina do admin
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Texto(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    link = models.URLField(max_length=200, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="textos")

# novamente mudança do nome para ficar mais facil a referenciação
    def __str__(self):
        return self.title
    
class Video(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    link = models.URLField(max_length=200, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="videos")
    


class ForumMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
