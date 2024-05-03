from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Campos personalizados
    #username = models.CharField(max_length=100, blank=False)
    sobrenome = models.CharField(max_length=100, blank=False)
    #cep = models.CharField(max_length=9, blank=False)
    #endereco = models.CharField(max_length=255, blank=False)
    #numero = models.CharField(max_length=10, blank=False)
    #bairro = models.CharField(max_length=100, blank=False)
    #cidade = models.CharField(max_length=100, blank=False)
    #uf = models.CharField(max_length=2, blank=False)
######
    def __str__(self):
        return self.username
