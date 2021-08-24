from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=255, verbose_name='Nome categoria')

    def __str__(self):
        return self.nome_categoria

