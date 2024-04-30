from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('cadastrar', cadastrar_usuario, name="cadastrar_usuario"),
    path('index', index, name="index"),
]
