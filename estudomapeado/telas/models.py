from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.urls import reverse


class CategoryTexto(models.Model):
    name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('categoria_textos', args=[self.id])

    # Fazendo a mudança do nome na pagina do admin
    class Meta:
        verbose_name_plural = "CategoriasTexto"

    def __str__(self):
        return self.name


class CategoryVideo(models.Model):
    name = models.CharField(max_length=30)

    # Fazendo a mudança do nome na pagina do admin
    class Meta:
        verbose_name_plural = "CategoriasVideo"

    def __str__(self):
        return self.name


class Texto(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    link = models.URLField(max_length=200, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField("CategoryTexto", related_name="textos")

    # novamente mudança do nome para ficar mais facil a referenciação
    def __str__(self):
        return self.title


class Comentario(models.Model):
    texto = models.ForeignKey(Texto, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário por {self.autor.username} em {self.texto.title}'


class Video(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    link = models.URLField(max_length=200, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("CategoryVideo", related_name="videos")


class ForumMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


#modelo para inserção de categoria no formulario
class TextoForm(forms.ModelForm):
    new_category = forms.CharField(required=False, help_text="Ou escreva uma nova categoria")

    class Meta:
        model = Texto
        fields = ['title', 'body', 'link', 'categories']

    def __init__(self, *args, **kwargs):
        super(TextoForm, self).__init__(*args, **kwargs)
        self.fields['categories'].required = False

    def save(self, commit=True):
        instance = super(TextoForm, self).save(commit=False)

        # Cria uma nova categoria se necessário
        if self.cleaned_data['new_category']:
            new_category, created = CategoryTexto.objects.get_or_create(name=self.cleaned_data['new_category'])
            instance.save()
            instance.categories.add(new_category)
        else:
            instance.save()

        if commit:
            instance.save()
            self.save_m2m()

        return instance