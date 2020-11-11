from django.shortcuts import render

def entrar(request):
    frase = "esta é a frase da entrar autenticação"
    return render(request, 'autenticacao/entrar.html', {'frase': frase})

def cadastro(request):
    frase = "esta é a frase da cadastro autenticação"
    return render(request, 'autenticacao/cadastro.html', {'frase': frase})