from django.contrib import admin

from .models import Loja

class LojaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

admin.site.register(Loja, LojaAdmin)