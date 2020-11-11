from django.shortcuts import render

def index(request):
    frase = "Esta frase está sendo exibida pela página index.html de carrinho."
    return render(request, 'carrinho/index.html', {'frase': frase})