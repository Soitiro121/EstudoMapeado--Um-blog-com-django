from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True),
         name='login'),
    path('cria_conta/', views.cria_conta, name='cria_conta'),
    path('altera_senha/', altera_senha, name='altera_senha'),
    path('termos/', views.termos, name='termos'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('textos/', views.list_textos, name='textos'),
    path('home/', views.home, name='home'),
    path('videos/', views.list_videos, name='videos'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('video/', views.list_video, name='video'),
]
