from django.db import models
from django.utils.text import slugify

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100, db_index = True, unique = True)
    slug = models.SlugField(max_length=100, default = '')

    class Meta:
        db_table = 'categoria'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        value = self.nome
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
