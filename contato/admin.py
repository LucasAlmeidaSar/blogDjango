from django.contrib import admin
from contato.models import Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_contato', 'email_contato', 'data_contato','resolvido_contato',)
    list_display_links = ('id', 'nome_contato', 'email_contato', 'data_contato',)
    list_editable = ('resolvido_contato',)
    list_filter = ('data_contato', 'resolvido_contato',)

admin.site.register(Contato, ContatoAdmin)
