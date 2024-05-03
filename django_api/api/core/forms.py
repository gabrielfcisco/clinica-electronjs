from django import forms
from core.models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nome', 'sobrenome', 'cep', 'endereco', 'numero', 'bairro', 'cidade', 'uf']
