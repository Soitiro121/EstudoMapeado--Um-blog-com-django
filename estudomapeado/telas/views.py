from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect


def cria_conta(request):
    if request.method == 'POST':
        # Obter dados do formulário
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmacao_senha = request.POST.get('confirmacao_senha')
        tipo_usuario = request.POST.get('userType')  # 'aluno' ou 'professor'

        # Validação básica
        if senha == confirmacao_senha:
            try:
                # Criar novo usuário
                user = User.objects.create_user(
                    username=email,  # Certifique-se de que o username é único
                    email=email,
                    password=senha,
                    first_name=nome_completo.split(' ')[0],
                    last_name=' '.join(nome_completo.split(' ')[1:])
                )

                # Adicionar usuário ao grupo correspondente
                if tipo_usuario == 'aluno':
                    group_name = 'Aluno'
                else:
                    group_name = 'Professor'

                group, _ = Group.objects.get_or_create(name=group_name)
                user.groups.add(group)

                # Redirecionar para a página de login ou outra página conforme necessário
                return redirect('login')

            except Exception as e:
                # Log a exceção ou informe ao usuário
                print(e)  # Exemplo básico
                # adicionar um retorno para informar o usuário do erro

    # Renderizar formulário de cadastro para método GET
    return render(request, 'cria_conta.html')  # Substitua 'cria_conta.html' pelo seu template


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'userprofile'):
                if user.userprofile.is_student:
                    return redirect('student_home')
                elif user.userprofile.is_teacher:
                    return redirect('teacher_home')
        else:
            # Invalid login
            pass



@login_required
def student_home(request):
    # Verifique novamente se o usuário é um estudante
    if not request.user.userprofile.is_student:
        return redirect('login')
    # Renderize o template para estudantes
    return render(request, 'estudante_home.html')


@login_required
def teacher_home(request):
    # Verifique novamente se o usuário é um professor
    if not request.user.userprofile.is_teacher:
        return redirect('login')
    # Renderize o template para professores
    return render(request, 'professor_home.html')
