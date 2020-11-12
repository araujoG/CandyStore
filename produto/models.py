from django.db import models
from categoria.models import Categoria

# Create your models here.
class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete = models.DO_NOTHING)
    nome = models.CharField(max_length=100, db_index = True, unique = True)
    slug = models.SlugField(max_length=100)
    imagem = models.CharField(max_length = 80, blank = True)
    qtdEstoque = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=5, decimal_places=2, default = 89.9)
    disponivel = models.BooleanField(default=False)
    dataCadastro = models.DateField(auto_now=True)
    secao = models.SlugField(max_length=50)

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return self.nome
