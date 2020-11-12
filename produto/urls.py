from django.urls import path

from produto import views

app_name = 'produto'

urlpatterns = [
    path('<int:id>/<slug:slugProduto>/', views.paginaProduto, name='paginaProduto')
]