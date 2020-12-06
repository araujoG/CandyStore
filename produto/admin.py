from django.contrib import admin
from .models import Produto
import random
from loja.models import Loja

def aumentaPreco(modeladmin, request, queryset):
    for p in queryset:
        p.preco = p.preco + 1
        p.save()
aumentaPreco.short_description = "Aumenta o Preço"

def aumentaEstoque(modeladmin, request, queryset):
    for p in queryset:
        p.qtdEstoque = p.qtdEstoque + 10
        p.save()
aumentaEstoque.short_description = "Aumenta o Estoque"

def zeraEstoque(modeladmin, request, queryset):
    for p in queryset:
        p.qtdEstoque = 0
        p.save()
zeraEstoque.short_description = "Zera o Estoque"


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'categoria', 'avaliacao', 'preco', 'disponivel']
    search_fields = ['nome', 'imagem']
    list_filter = ['categoria']
    prepopulated_fields = {'slug': ('nome',)}
    actions = [aumentaPreco, aumentaEstoque, zeraEstoque]
    save_as = True

admin.site.register(Produto, ProdutoAdmin)
