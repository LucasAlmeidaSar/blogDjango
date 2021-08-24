from django.contrib.auth.models import User
from django.db import models
from posts.models import Post


class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
    email_comentario = models.EmailField(verbose_name='E-mail')
    conteudo_comentario = models.TextField(verbose_name='Comentário')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    autor_post_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor do post', blank=True, null=True)
    data_comentario = models.DateTimeField(auto_now_add=True)
    publicado_comentario = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return 'Comentário de: ' + self.nome_comentario