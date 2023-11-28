from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from . models import *
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.db import IntegrityError


def cria_conta(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmacao_senha = request.POST.get('confirmacao_senha')
        tipo_usuario = request.POST.get('userType')

        if senha != confirmacao_senha:
            # Adicionar mensagem de erro
            return render(request, 'cria_conta.html', {'error': 'As senhas não coincidem'})

        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=senha,
                first_name=nome_completo.split(' ')[0],
                last_name=' '.join(nome_completo.split(' ')[1:])
            )

            group_name = 'Estudante' if tipo_usuario == 'Estudante' else 'Professor'
            group, _ = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)

            return redirect('login')  # Substitua 'login' pelo nome da sua URL de login

        except Exception as e:
            # Log a exceção ou informe ao usuário
            return render(request, 'cria_conta.html', {'error': str(e)})

    return render(request, 'cria_conta.html')


@login_required
def home(request):
    context = {'is_estudante': request.user.groups.filter(name='Estudante').exists(),
               'is_professor': request.user.groups.filter(name='Professor').exists()}
    return render(request, 'home.html', context)


def altera_senha(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nova_senha = request.POST.get('nova_senha')
        confirmacao_senha = request.POST.get('confirmacao_senha')

        if nova_senha == confirmacao_senha:
            try:
                user = User.objects.get(email=email)
                user.password = make_password(nova_senha)
                user.save()

                messages.success(request, 'Senha alterada com sucesso.')
                return redirect('login')  # Substitua pelo nome da sua URL de login
            except User.DoesNotExist:
                messages.error(request, 'Usuário não encontrado.')

        else:
            messages.error(request, 'As senhas não coincidem.')

    return render(request, 'altera_senha.html')


def termos(request):
    return render(request, 'termos.html')


def sucesso(request):
    return render(request, 'sucesso.html')


def list_textos(request):
    texto_list = Texto.objects.all()
    context = {'texto_list': texto_list}
    return render(request, 'textos.html', context)


def list_videos(request):
    video_list = Video.objects.all()
    context = {'video_list': video_list}
    return render(request, 'videos.html', context)


def list_video(request):
    video_list = Video.objects.all()
    context = {'video_list': video_list}
    return render(request, 'video.html', context)