from django.db import models
from categoria.models import Categoria
from loja.models import Loja
from django.utils.text import slugify
from django.urls import reverse
from decimal import Decimal

# Create your models here.


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, default="", null=True)
    nome = models.CharField(max_length=100, db_index=True, unique=True)
    slug = models.SlugField(max_length=100, default='')
    marca = models.CharField(max_length=50, db_index=True, default="")
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    imagem = models.CharField(max_length=80)
    loja = models.ForeignKey(Loja, max_length=100, on_delete=models.PROTECT, default="")
    estoque = models.IntegerField(default=0)
    disponivel = models.BooleanField(default=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2, default=89.9)
    dataCadastro = models.DateField(auto_now=True)
    secao = models.SlugField(max_length=50, default="")
    descricao = models.CharField(max_length=1500, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam gravida elit nec sapien interdum sagittis. Nulla dignissim erat eu mauris dignissim, ac vestibulum est laoreet. Phasellus sapien metus, cursus a tempus at, viverra laoreet sapien. Donec ullamcorper sit amet nibh eget aliquam. Donec sodales mattis orci, ut consequat tortor pretium eu. Pellentesque tincidunt, nunc non condimentum mattis, metus risus dignissim lacus, at consequat justo odio sit amet dui. Proin sed ultricies nunc. \nLorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam gravida elit nec sapien interdum sagittis. Nulla dignissim erat eu mauris dignissim, ac vestibulum est laoreet. Phasellus sapien metus, cursus a tempus at, viverra laoreet sapien. Donec ullamcorper sit amet nibh eget aliquam. Donec sodales mattis orci, ut consequat tortor pretium eu. Pellentesque tincidunt, nunc non condimentum mattis, metus risus dignissim lacus, at consequat justo odio sit amet dui. Cras ut metus eleifend est ultricies aliquam vel sit amet ante. In dignissim pellentesque suscipit. Vivamus at nisi dapibus, accumsan neque in, consectetur nunc. Nam efficitur ex faucibus, imperdiet ex eget, vehicula purus. Donec commodo sagittis hendrerit.")

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        value = self.nome
        self.slug = slugify(value, allow_unicode=False)
        super().save(*args, **kwargs)

    def getAbsoluteUrl(self):
        return reverse('produto:paginaProduto', args=[self.id, self.slug])

    def precoOriginal(self):
        return float(self.preco)*1

    def getPrecoParcelado(self):
        return ((float(self.preco)/10)//0.01)/100
