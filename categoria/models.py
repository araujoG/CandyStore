from django.db import models
from django.utils.text import slugify

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100, db_index = True, unique = True)
    imagem = models.CharField(max_length=80, blank = True)
    descricao = models.TextField(max_length=800, default="",blank = True)
    slug = models.SlugField(max_length=100, default = '',blank = True)

    class Meta:
        db_table = 'categoria'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        value = self.nome
        if(self.descricao == ""):
            self.descricao = "Venha conferir as melhores opções de " + self.nome + " você só encontra aqui"
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    
    def getNumeroProdutos(self):
        return self.produto_set.count()