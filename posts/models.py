from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from categorias.models import Categoria

class Post(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name='Título post')
    categoria_post = models.ForeignKey(Categoria, blank=True, null=True,
                                       on_delete=models.DO_NOTHING, verbose_name='Categoria post')
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor do post')
    data_post = models.DateTimeField(auto_now_add=True, verbose_name='Data do post')
    excerto_post = models.TextField(verbose_name='Excerto')
    conteudo_post = models.TextField(verbose_name='Conteúdo do post')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', verbose_name='Imagem', blank=True, null=True)
    publicado_post = models.BooleanField(default=False, verbose_name='Publicado')
    posts = models.Manager()

    def __str__(self):
        return self.titulo_post