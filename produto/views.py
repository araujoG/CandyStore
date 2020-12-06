from django.shortcuts import get_object_or_404, redirect, render
from produto.models import Produto
from django.core.paginator import Paginator
from produto.forms import PesquisaProdutoForm, ProdutoEmMassaForm, ProdutoForm, QuantidadeForm
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from django.template import loader

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


def interfaceAdmin(request):
    print("passou aqui pela view")
    form = PesquisaProdutoForm(request.GET)
    if form.is_valid(): 
        nome = form.cleaned_data['nome']
        produtos = Produto.objects.filter(nome__icontains=nome)
        paginator = Paginator(produtos, 8)
        pagina = request.GET.get('pagina')
        pageObject = paginator.get_page(pagina)
        return render(request, 'produto/interfaceAdmin.html', {'produtos': pageObject, 'form':form, 'nomePesquisado': nome})
    else:
        raise ValueError("Ocorreu um erro inesperado ao tentar recuperar um produto....")

def cadastraProduto(request):
    if request.POST:
        idProduto = request.session.get('produtoEditado')
        print('idProduto na sessão = ' + str(idProduto))
        if idProduto:
            produto = get_object_or_404(Produto, pk=idProduto)
            produtoForm = ProdutoForm(request.POST, instance=produto)
        else:
            produtoForm = ProdutoForm(request.POST)

        if produtoForm.is_valid():
            produto = produtoForm.save(commit=False)
            produto.save()
            if idProduto:
                messages.add_message(request, messages.INFO, 'Produto alterado com sucesso!')
                del request.session['produtoEditado']
            else:
                messages.add_message(request, messages.INFO, 'Produto cadastrado com sucesso!')

            return redirect('produto:paginaProduto', id=produto.id, slugProduto=produto.slug)
    else:
        try:
            del request.session['produtoEditado']
        except KeyError:
            pass
        produtoForm = ProdutoForm()

    return render(request, 'produto/cadastraProduto.html', {'form': produtoForm})

def editaProduto(request, id, slugProduto):
    produto = get_object_or_404(Produto, pk=id)
    produtoForm = ProdutoForm(instance=produto)
    request.session['produtoEditado'] = id
    return render(request, 'produto/cadastraProduto.html', {'form': produtoForm})


def removeProduto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()
    messages.add_message(request, messages.INFO, 'Produto removido com sucesso.')
    return render(request, 'produto/paginaProduto.html', {'produto': produto})


def cadastraProdutoEmMassa(request):
    if request.POST:
        produtoForm = ProdutoEmMassaForm(request.POST)
        if produtoForm.is_valid():
            produto = produtoForm.save(commit=False)
            produto.save()
            produtos = Produto.objects.all()
            total = 0
            for p in produtos:
                total += p.getValorEmEstoque()
            total = round(total, 2)
            item = {'id':produto.id, 'categoria': produto.categoria.nome, 'nome': produto.nome, 'preco': produto.preco, 'valorEmEstoque': produto.preco*produto.estoque, 'inputEstoque':QuantidadeForm(initial={'quantidade': produto.estoque, 'produtoId': produto.id}), 'estoqueItem': produto.estoque}
            template = loader.get_template('produto/rowEstoqueAtivo.html')
            rowTabela = template.render({'item': item}, request)
            return JsonResponse({'row': rowTabela, 'formValido':True, 'estoque': item['estoqueItem'], 'totalEmEstoque':total}, status=200)
        else:
            print("formulario inválido")
            # return JsonResponse({"formulario": produtoForm.as_p(), 'status':'erro'}, status=200)
            return render(request, 'produto/formEmMassa.html', {'form': produtoForm})
    else:
        produtos = Produto.objects.all()
        valorEmEstoque = 0.0
        listaDeItens = []
        for produto in produtos:
            valorEmEstoque += float(produto.preco) * float(produto.estoque)
            listaDeItens.append({'id':produto.id, 'categoria': produto.categoria.nome, 'nome': produto.nome, 'preco': produto.preco, 'valorEmEstoque': produto.preco*produto.estoque, 'inputEstoque':QuantidadeForm(initial={'quantidade': produto.estoque, 'produtoId': produto.id}), 'estoqueItem': produto.estoque})
        valorEmEstoque = round(valorEmEstoque, 2)
        produtoForm = ProdutoEmMassaForm()
    return render(request, 'produto/cadastraProdutoEmMassa.html', {'form': produtoForm, 'listaProdutos': listaDeItens, 'totalEmEstoque':valorEmEstoque})

def atualizaProdutoEmMassa(request):
    if request.POST:
        print("entrou em atualiza POST")
        quantidadeForm = QuantidadeForm(request.POST)
        if(quantidadeForm.is_valid()):
            id = quantidadeForm.cleaned_data['produtoId']
            qtd = quantidadeForm.cleaned_data['quantidade']
            produto = get_object_or_404(Produto, id=id)
            produto.estoque = qtd
            produto.save()
            produtos = Produto.objects.all()
            total = 0
            for p in produtos:
                total += p.getValorEmEstoque()
            total = round(total, 2)
            item = {'id':produto.id, 'categoria': produto.categoria.nome, 'nome': produto.nome, 'preco': produto.preco, 'valorEmEstoque': produto.preco*produto.estoque, 'inputEstoque':QuantidadeForm(initial={'quantidade': produto.estoque, 'produtoId': produto.id}), 'estoqueItem': produto.estoque}
            template = loader.get_template('produto/rowEstoqueAtivo.html')
            rowTabela = template.render({'item': item}, request)            
            return JsonResponse({'row': rowTabela, 'totalEmEstoque':total}, status=200)
    return redirect('produto:cadastraProdutoEmMassa')

def removeProdutoAjax(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()
    produtos = Produto.objects.all()
    total = 0
    for p in produtos:
        total += p.getValorEmEstoque()
    total = round(total, 2)
    return JsonResponse({'totalEmEstoque':round(total, 2)}, status=200)