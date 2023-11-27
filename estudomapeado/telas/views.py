from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *


def cria_conta(request):
    if request.method == 'POST':
        # Obter dados do formulário
        nome_completo = request.POST.get('nome-completo')
        email = request.POST.get('e-mail')  # Corrigido o nome do campo
        senha = request.POST.get('senha')
        confirmacao_senha = request.POST.get('confirmacao-da-senha')  # Corrigido o nome do campo
        tipos_usuario = request.POST.getlist('userType')  # Retorna uma lista com os valores marcados

        # Validação básica
        if senha == confirmacao_senha:
            try:
                # Criar novo usuário
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=senha,
                    first_name=nome_completo.split(' ')[0],
                    last_name=' '.join(nome_completo.split(' ')[1:])
                )

                # Adicionar usuário aos grupos correspondentes
                for tipo_usuario in tipos_usuario:
                    group_name = 'Estudante' if tipo_usuario == 'Estudante' else 'Professor'
                    group, _ = Group.objects.get_or_create(name=group_name)
                    user.groups.add(group)

                # Redirecionar para a página de login
                return redirect('login')

            except Exception as e:
                # Log a exceção ou informe ao usuário
                print(e)  # Exemplo básico
                # Aqui você pode adicionar um retorno para informar o usuário do erro

    # Renderizar formulário de cadastro para método GET
    return render(request, 'cria_conta.html')


@login_required
def home(request):
    context = {'is_aluno': request.user.groups.filter(name='Estudante').exists(),
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