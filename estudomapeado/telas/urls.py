# telas/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('cria_conta/', cria_conta, name='cria_conta'),
]
