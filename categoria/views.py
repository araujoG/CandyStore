from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from categoria.models import Categoria
from categoria.forms import CategoriaForm, PesquisaCategoriaForm
from produto.models import Produto
from django.contrib import messages
from produto.forms import ProdutoForm


def interfaceAdmin(request):
    form = PesquisaCategoriaForm(request.GET)
    if form.is_valid(): 
        nome = form.cleaned_data['nome']
        categorias = Categoria.objects.filter(nome__icontains=nome)
        paginator = Paginator(categorias, 8)
        pagina = request.GET.get('pagina')
        pageObject = paginator.get_page(pagina)
        return render(request, 'categoria/interfaceAdmin.html', {'categorias': pageObject, 'form':form, 'nomePesquisado': nome})
    else:
        raise ValueError("Ocorreu um erro inesperado ao tentar recuperar um produto....")

def cadastraCategoria(request):
    if request.POST:
        idCategoria = request.session.get('categoriaEditada')
        print('idCategoria na sessão = ' + str(idCategoria))
        if idCategoria:
            categoria = get_object_or_404(Categoria, pk=idCategoria)
            categoriaForm = CategoriaForm(request.POST, instance=categoria)
        else:
            categoriaForm = CategoriaForm(request.POST)

        if categoriaForm.is_valid():
            categoria = categoriaForm.save(commit=False)
            categoria.save()
            if idCategoria:
                messages.add_message(request, messages.INFO, 'Categoria alterado com sucesso!')
                del request.session['categoriaEditada']
            else:
                messages.add_message(request, messages.INFO, 'Categoria cadastrado com sucesso!')

            return redirect('categoria:interfaceAdmin')
    else:
        try:
            del request.session['categoriaEditada']
        except KeyError:
            pass
        categoriaForm = CategoriaForm()

    return render(request, 'categoria/cadastraCategoria.html', {'form': categoriaForm})

def editaCategoria(request, id, slugCategoria):
    categoria = get_object_or_404(Categoria, pk=id)
    categoriaForm = CategoriaForm(instance=categoria)
    request.session['categoriaEditada'] = id
    return render(request, 'categoria/cadastraCategoria.html', {'form': categoriaForm})

def removeCategoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    print(categoria)
    n = categoria.nome
    categoria.delete()
    messages.add_message(request, messages.INFO, "Categoria '" +n+ "' foi removida com sucesso.")
    return interfaceAdmin(request)