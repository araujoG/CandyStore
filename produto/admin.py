from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'avaliacao', 'preco', 'disponivel']
    search_fields = ['nome', 'imagem']
    list_filter = ['categoria']
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Produto, ProdutoAdmin)
