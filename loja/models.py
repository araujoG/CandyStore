from django.db import models

# Create your models here.

class Loja(models.Model):
    nome = models.CharField(max_length=100, unique = True, db_index = True)
    logo = models.CharField(max_length=100)

    class Meta:
        db_table = 'loja'

    def __str__(self):
        return self.nome