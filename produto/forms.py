from django import forms
from produto.models import Produto
from categoria.models import Categoria
from django.core.validators import MaxValueValidator, RegexValidator
from loja.models import Loja

class PesquisaProdutoForm(forms.Form):
    
    nome = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control mr-0', 'placeholder':'Pesquisar', 'aria-label':'Pesquisar'}),
        required = False,
    )

class ProdutoForm(forms.ModelForm):
    
    class Meta:
        model = Produto
        fields = ('nome', 'categoria', 'marca', 'avaliacao', 'imagem', 'loja', 'estoque', 'disponivel', 'preco', 'descricao')
        localized_fields = ('preco','avaliacao',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages={'required': 'Campo obrigatório.',
                                            'unique': 'Nome de produto duplicado.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control','id':'inputNomeProduto','placeholder':'Nome do Produto'})

        self.fields['categoria'].error_messages={'required': 'Campo obrigatório'}
        self.fields['categoria'].queryset=Categoria.objects.all().order_by('nome')
        self.fields['categoria'].empty_label='--- Selecione uma categoria ---'
        self.fields['categoria'].widget.attrs.update({'class': 'form-control','id':'inputCategoria'})

        self.fields['marca'].error_messages={'required': 'Campo obrigatório'}
        self.fields['marca'].widget.attrs.update({'class': 'form-control','id':'inputMarca','placeholder':'Marca do Produto'})

        self.fields['avaliacao'].min_value=0
        self.fields['avaliacao'].error_messages={'required': 'Campo obrigatório.',
                                             'invalid': 'Valor inválido.',
                                             'max_digits': 'Mais de 2 dígitos no total.',
                                             'max_decimal_places': 'Mais de 1 dígito decimal.',
                                             'max_whole_digits': 'Mais de 1 dígito inteiro.'}
        self.fields['avaliacao'].widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id':'inputAvaliaca',
            'placeholder':'Avaliação do Produto',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })

        self.fields['imagem'].error_messages={'required': 'Campo obrigatório'}
        self.fields['imagem'].validators=[
            RegexValidator(regex='^[a-z]+\.(jpg|png|gif|bmp)$', message='Nome de imagem inválido.')]
        self.fields['imagem'].widget.attrs.update({'class': 'form-control','id':'inputImagem','placeholder':'Nome do Arquivo de Imagem'})
        self.fields['imagem'].required = True

        self.fields['loja'].error_messages={'required': 'Campo obrigatório'}
        self.fields['loja'].queryset=Loja.objects.all().order_by('nome')
        self.fields['loja'].empty_label='--- Selecione uma loja ---'
        self.fields['loja'].widget.attrs.update({'class': 'form-control','id':'inputLoja'})

        self.fields['estoque'].min_value=0
        self.fields['estoque'].widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id':'inputEstoque',
            'placeholder':'Quantidade em Estoque',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)'
        })

        # self.fields['disponivel'].widget.attrs.update({'class':'custom-control-input'})

        self.fields['preco'].min_value=0
        self.fields['preco'].error_messages={'required': 'Campo obrigatório.',
                                             'invalid': 'Valor inválido.',
                                             'max_digits': 'Mais de 5 dígitos no total.',
                                             'max_decimal_places': 'Mais de 2 dígitos decimais.',
                                             'max_whole_digits': 'Mais de 3 dígitos inteiros.'}
        self.fields['preco'].widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id':'inputPreco',
            'placeholder':'Preço',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })
        
        self.fields['descricao'].error_messages={'required': 'Campo obrigatório'}
        self.fields['descricao'].widget.attrs.update({'class': 'form-control','id':'inputDescricao'})

class ProdutoEmMassaForm(forms.ModelForm):
    
    class Meta:
        model = Produto
        fields = ('nome', 'categoria', 'marca', 'loja', 'imagem', 'estoque', 'preco',)
        localized_fields = ('preco',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages={'required': 'Campo obrigatório.',
                                            'unique': 'Nome de produto duplicado.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control','id':'inputNomeProduto','placeholder':'Nome do Produto'})

        self.fields['categoria'].error_messages={'required': 'Campo obrigatório'}
        self.fields['categoria'].queryset=Categoria.objects.all().order_by('nome')
        self.fields['categoria'].empty_label='--- Selecione uma categoria ---'
        self.fields['categoria'].widget.attrs.update({'class': 'form-control','id':'inputCategoria'})



        #### A partir daqui os campos devem ter valores iniciais pois não são importantes ########
        
        self.fields['marca'].initial = "Sem Marca"
        self.fields['marca'].error_messages={'required': 'Campo obrigatório'}
        self.fields['marca'].widget.attrs.update({'class': 'form-control','id':'inputMarca','placeholder':'Marca do Produto'})

        self.fields['loja'].initial = Loja.objects.get(id=1)
        self.fields['loja'].error_messages={'required': 'Campo obrigatório'}
        self.fields['loja'].queryset=Loja.objects.all().order_by('nome')
        self.fields['loja'].empty_label='--- Selecione uma loja ---'
        self.fields['loja'].widget.attrs.update({'class': 'form-control','id':'inputLoja'})

        self.fields['imagem'].initial="memamendoim.png" #imagem padrão
        self.fields['imagem'].error_messages={'required': 'Campo obrigatório'}
        self.fields['imagem'].validators=[
            RegexValidator(regex='^[a-z]+\.(jpg|png|gif|bmp)$', message='Nome de imagem inválido.')]
        self.fields['imagem'].widget.attrs.update({'class': 'form-control','id':'inputImagem','placeholder':'Nome do Arquivo de Imagem'})
        self.fields['imagem'].required = True


        self.fields['estoque'].min_value=0
        self.fields['estoque'].widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id':'inputEstoque',
            'placeholder':'Quantidade em Estoque',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)'
        })

        # self.fields['disponivel'].widget.attrs.update({'class':'custom-control-input'})

        self.fields['preco'].min_value=0
        self.fields['preco'].error_messages={'required': 'Campo obrigatório.',
                                             'invalid': 'Valor inválido.',
                                             'max_digits': 'Mais de 5 dígitos no total.',
                                             'max_decimal_places': 'Mais de 2 dígitos decimais.',
                                             'max_whole_digits': 'Mais de 3 dígitos inteiros.'}
        self.fields['preco'].widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id':'inputPreco',
            'placeholder':'Preço',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })

class QuantidadeForm(forms.Form):
    
    produtoId = forms.CharField(widget=forms.HiddenInput())

    quantidade = forms.IntegerField(
        min_value=0,
        max_value=99,
        widget=forms.TextInput(attrs={'class': 'form-control btn-light quantidade mx-auto',
                                      'style': 'text-align: center; background-color: #6c757d; width: 70px;',
                                      'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)'}),
        required=True
    )