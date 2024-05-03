from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from core.forms import CustomUserCreationForm
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
    users = CustomUser.objects.all()
    return render(request, '[nome].html', {'users': users})

def editUsers(request, user_id):
    # Recupere o usuário existente pelo ID
    user = get_object_or_404(CustomUser, pk=user_id)

    if request.method == "POST":
        # Preencha o formulário com os dados do usuário e dados POST
        form = CustomUserForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        # Preencha o formulário com os dados do usuário existente
        form = CustomUserForm(instance=user)

    return render(request, '[nome].html', {'form_usuario': form})
