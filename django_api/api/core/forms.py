from django.contrib.auth.forms import UserCreationForm
from core.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2')
#, 'nome', 'sobrenome', 'cep', 'endereco', 'numero', 'bairro', 'cidade', 'uf'