from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import Group


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
    

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    texto = models.ForeignKey("Texto", on_delete=models.CASCADE)

# apenas mudança de nome
    def __str__(self):
        return f"{self.author} on '{self.post}'"


Group.objects.get_or_create(name='Estudante')
Group.objects.get_or_create(name='Professor')