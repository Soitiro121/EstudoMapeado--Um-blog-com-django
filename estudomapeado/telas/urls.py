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
    path('termos_logado/', views.termos_logado, name='termos_logado'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('textos/', views.list_textos, name='textos'),
    path('home/', views.home, name='home'),
    path('videos/', views.list_videos, name='videos'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('sumario/', views.list_sumario, name='sumario'),
    path('detail_textos/<int:texto_id>/', views.detail_textos, name='detail_textos'),
    path('detail_videos/<int:video_id>/', views.detail_videos, name='detail_videos'),
    path('criar_texto/', views.criar_texto, name='criar_texto'),
    path('criar_video/', views.criar_video, name='criar_video'),
    path('salvar_texto/', views.salvar_texto, name='salvar_texto'),
    path('salvar_video/', views.salvar_video, name='salvar_video'),
    path('forum/', forum_view, name='forum_view'),
    path('forum/post/', forum_post, name='forum_post'),
    path('categorias/<int:categoria_id>/', views.categoria_textos, name='categoria_textos'),
]
