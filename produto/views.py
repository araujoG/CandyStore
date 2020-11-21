from django.shortcuts import get_object_or_404, render
from produto.models import Produto
from django.core.paginator import Paginator
from produto.forms import PesquisaProdutoForm

def paginaProduto(request,id,slugProduto):
    produto = get_object_or_404(Produto, id = id )
    return render(request, 'produto/paginaProduto.html', {'produto': produto})

def listaProduto(request):
    form = PesquisaProdutoForm(request.GET)
    if form.is_valid(): 
        nome = form.cleaned_data['nome']
        produtos = Produto.objects.filter(nome__icontains=nome)
        paginator = Paginator(produtos, 8)
        pagina = request.GET.get('pagina')
        pageObject = paginator.get_page(pagina)
        print(produtos)
        print(pageObject)
        return render(request, 'produto/listaProduto.html', {'produtos': pageObject, 'form':form, 'nomePesquisado': nome})
    else:
        raise ValueError("Ocorreu um erro inesperado ao tentar recuperar um produto....")