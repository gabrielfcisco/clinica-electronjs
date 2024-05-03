from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('cadastrar', cadastrar, name="cadastrar"),
    path('index', index, name="index"),
    path('', login, name="login"),
]
