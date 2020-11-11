from django.shortcuts import render

def index(request):
    frase = "esta é a frase da index candyStore"
    return render(request, 'index.html', {'frase': frase})