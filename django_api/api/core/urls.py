from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('cadastrar', cadastrar, name="cadastrar"),
    path('index', getUsers, name="index"),
    path('', loginUser, name="login"),
    path('logout', logoutUser, name="logout"),
    path('edit_user/<int:user_id>/', editUsers, name='edit_user'),
    path('delete_user/<int:user_id>/', delete_user, name="delete_user"),
]
