from django.shortcuts import render
from produto.models import Produto

def index(request):
    frase = "esta é a frase da index candyStore"
    maisVendidos = Produto.objects.filter(secao='maisVendidos')
    lancamentos = Produto.objects.filter(secao='lancamentos')
    hp = Produto.objects.filter(secao='hp')
    
    return render(request, 'index.html', {'maisVendidos': maisVendidos, 'lancamentos' : lancamentos, 'hp' : hp})