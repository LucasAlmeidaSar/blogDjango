from django.db import models

class Contato(models.Model):
    nome_contato = models.CharField(max_length=150, verbose_name='Nome')
    email_contato = models.EmailField(verbose_name='E-mail')
    assunto_contato = models.CharField(max_length=150, verbose_name='Assunto')
    conteudo_contato = models.TextField(verbose_name='Mensagem')
    data_contato = models.DateTimeField(auto_now_add=True)
    resolvido_contato = models.BooleanField(default=False, verbose_name='Resolvido')

    def __str__(self):
        return 'Contato de: ' + self.nome_contato