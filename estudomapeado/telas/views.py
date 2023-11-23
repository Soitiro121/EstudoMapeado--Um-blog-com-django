# telas/views.py
from django.shortcuts import render

def login_page(request):
    return render(request, 'telas/login_page.html')
