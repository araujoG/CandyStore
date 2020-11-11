from django.shortcuts import render

def index(request):
    frase = "Esta frase está sendo exibida pela página index.html de produto."
    return render(request, 'produto/index.html', {'frase': frase})