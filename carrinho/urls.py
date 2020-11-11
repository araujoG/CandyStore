from django.contrib import admin
from django.urls import include, path
from carrinho import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.index, name="index"),
]