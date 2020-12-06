from django.urls import path

from produto import views

app_name = 'produto'

urlpatterns = [
    path('<int:id>/<slug:slugProduto>/', views.paginaProduto, name='paginaProduto'),
    path('', views.listaProduto, name='listaProduto'),
    path('administrar/', views.interfaceAdmin, name='interfaceAdmin'),
    path('administrar/cadastro', views.cadastraProduto, name='cadastraProduto'),
    path('administrar/cadastroEmMassa/atualiza', views.atualizaProdutoEmMassa, name='atualizaProdutoEmMassa'),
    path('administrar/cadastroEmMassa', views.cadastraProdutoEmMassa, name='cadastraProdutoEmMassa'),
    path('administrar/edita/<int:id>/<slug:slugProduto>/', views.editaProduto, name='editaProduto'),
    path('administrar/remove/<int:id>/', views.removeProduto, name='removeProduto'),
    path('administrar/removeAjax/<int:id>/', views.removeProdutoAjax, name='removeProdutoAjax')
]