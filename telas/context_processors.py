# context_processors.py
# Para evitar a repetição de código usamos o context_processors
# para verificar em todas as templates a condição do usuário
# mostrando apenas os conteúdos endereçados ao grupo

def group_check(request):
    return {
        'is_estudante': request.user.groups.filter(name='Estudante').exists(),
        'is_professor': request.user.groups.filter(name='Professor').exists()
    }
