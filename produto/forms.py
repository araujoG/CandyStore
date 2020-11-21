from django import forms

class PesquisaProdutoForm(forms.Form):
    
    nome = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mr-0', 'placeholder':'Pesquisar', 'aria-label':'Pesquisar'}),
        required = False,
    )