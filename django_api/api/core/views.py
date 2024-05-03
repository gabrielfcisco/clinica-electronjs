from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from core.forms import CustomUserCreationForm
from core.models import CustomUser
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        # Se o usuário não estiver autenticado, redirecione-o para a página de login
        return redirect(reverse('login'))

    # O código aqui será executado apenas se o usuário estiver autenticado
    return render(request, 'index.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Detalhes de login inválidos.'})
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')  # Substitua 'página_inicial' pelo nome da sua URL inicial
                  
def cadastrar(request):
    if request.method == "POST":
        form_usuario = CustomUserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = CustomUserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})

def getUsers(request):
    if not request.user.is_authenticated:
        # Se o usuário não estiver autenticado, redirecione-o para a página de login
        return redirect(reverse('login'))
    users = CustomUser.objects.all()
    return render(request, 'index.html', {'users': users})

def editUsers(request, user_id):
    if not request.user.is_authenticated:
        # Se o usuário não estiver autenticado, redirecione-o para a página de login
        return redirect(reverse('login'))

    # Recupere o usuário existente pelo ID
    user = get_object_or_404(CustomUser, pk=user_id)

    if request.method == "POST":
        # Preencha o formulário com os dados do usuário e dados POST
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        # Preencha o formulário com os dados do usuário existente
        form = CustomUserCreationForm(instance=user)

    return render(request, 'editar.html', {'form_usuario': form})

def delete_user(request, user_id):
    if not request.user.is_authenticated:
        # Se o usuário não estiver autenticado, redirecione-o para a página de login
        return redirect(reverse('login'))

    user = get_object_or_404(CustomUser, pk=user_id)
    
    if request.method == 'POST':
        user.delete()
        print("Usuário excluído com sucesso:", user_id)
        return redirect('index')

    return render(request, 'index.html', {'user': user})
