# telas/views.py
from django.shortcuts import render


def index(request):
    return render(request, 'telas/index.html')


def cria_conta(request):
    return render(request, 'telas/cria_conta.html')
