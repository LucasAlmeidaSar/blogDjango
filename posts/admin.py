from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titulo_post', 'categoria_post', 'autor_post', 'data_post', 'publicado_post',)
    list_display_links = ('id', 'titulo_post', 'categoria_post', 'autor_post', 'data_post', )
    list_editable = ('publicado_post',)
    summernote_fields = ('conteudo_post',)
    list_filter = ('categoria_post', 'data_post')


admin.site.register(Post, PostAdmin)