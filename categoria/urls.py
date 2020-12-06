from django.urls import path

from categoria import views

app_name = 'categoria'

urlpatterns = [
    path('administrar/', views.interfaceAdmin, name='interfaceAdmin'),
    path('administrar/cadastro', views.cadastraCategoria, name='cadastraCategoria'),
    path('administrar/edita/<int:id>/<slug:slugCategoria>/', views.editaCategoria, name='editaCategoria'),
    path('administrar/remove/<int:id>/', views.removeCategoria, name='removeCategoria')

]