from django.contrib import admin
from django.urls import include, path
from autenticacao import views

app_name = 'autenticacao'

urlpatterns = [
    path('entrar/', views.entrar, name="entrar"),
    path('cadastro/', views.cadastro, name="cadastro"),
]
