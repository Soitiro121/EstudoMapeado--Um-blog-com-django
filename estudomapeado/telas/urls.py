from django.urls import path
from django.views.generic.base import RedirectView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('cria_conta/', views.cria_conta, name='cria_conta'),
    path('student/home/', views.student_home, name='student_home'),
    path('teacher/home/', views.teacher_home, name='teacher_home'),
    path('', RedirectView.as_view(url='/login/', permanent=True)),  # Redirecionamento para login
]
