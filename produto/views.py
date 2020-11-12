from django.shortcuts import get_object_or_404, render
from produto.models import Produto

def paginaProduto(request,id,slugProduto):
    produto = get_object_or_404(Produto, id = id )
    return render(request, 'produto/paginaProduto.html', {'produto': produto})