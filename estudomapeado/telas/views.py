from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from . models import *
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404


def cria_conta(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmacao_senha = request.POST.get('confirmacao_senha')
        tipo_usuario = request.POST.get('userType')

        if senha != confirmacao_senha:
            print("Senha incorreta")
            return render(request, 'criar_conta.html', {'error': 'As senhas não coincidem'})

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

            return redirect('login')

        except Exception as e:
            print("Erro")
            return render(request, 'criar_conta.html', {'error': str(e)})

    return render(request, 'criar_conta.html')


@login_required
def home(request):
    return render(request, 'home.html')


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
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'Usuário não encontrado.')

        else:
            messages.error(request, 'As senhas não coincidem.')

    return render(request, 'altera_senha.html')


def termos(request):
    return render(request, 'termos.html')

def termos_logado(request):
    return render(request, 'termos_logado.html')


def sucesso(request):
    return render(request, 'sucesso.html')


@login_required
def list_textos(request):
    textos = Texto.objects.all()

    # Adicionando uma prévia para cada texto
    for texto in textos:
        texto.preview = texto.body[:250]  # Corta os primeiros 100 caracteres

    context = {'textos': textos}
    return render(request, 'textos.html', context)


@login_required
def list_videos(request):
    video_list = Video.objects.all()
    context = {'video_list': video_list}
    return render(request, 'videos.html', context)


@login_required
def list_video(request):
    video_list = Video.objects.all()
    context = {'video_list': video_list}
    return render(request, 'video.html', context)

@login_required
def list_sumario(request):
    sumario_list = Sumario.objects.all()
    context = {'sumario_list': sumario_list}
    return render(request, 'sumario.html', context)


@login_required
def detail_textos(request, texto_id):
    texto = get_object_or_404(Texto, pk=texto_id)
    return render(request, 'detail_textos.html', {'texto': texto})

@login_required
def detail_videos(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'detail_videos.html', {'video': video})


@login_required
def criar_texto(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        novo_texto = Texto(title=title, body=body)
        novo_texto.save()
        return redirect('textos')

    return render(request, 'criar_texto.html')


@login_required
def salvar_texto(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        link = request.POST.get('link')
        novo_texto = Texto(title=title, body=body, link=link)
        novo_texto.save()

        return redirect('textos')

    return render(request, 'criar_texto.html')


@login_required
def criar_texto(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        novo_texto = Texto(title=title, body=body)
        novo_texto.save()
        return redirect('textos')

    return render(request, 'criar_texto.html')


@login_required
def salvar_texto(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        link = request.POST.get('link')
        novo_texto = Texto(title=title, body=body, link=link)
        novo_texto.save()

        return redirect('textos')

    return render(request, 'criar_texto.html')
