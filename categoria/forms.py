from django import forms
from categoria.models import Categoria

class PesquisaCategoriaForm(forms.Form):
    
    nome = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mr-0', 'placeholder':'Pesquisar Categoria', 'aria-label':'Pesquisar Categoria'}),
        required = False,
    )

class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = ('nome','imagem', 'descricao')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control w-85','placeholder':'Nome da Categoria'})
        self.fields['imagem'].widget.attrs.update({'class': 'form-control w-85','placeholder':'Caminho da Imagem'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control w-85','placeholder':'Descrição da Categoria'})