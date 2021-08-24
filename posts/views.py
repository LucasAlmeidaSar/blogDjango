from django.contrib import messages
from django.db.models import Q, Count, Case, When
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from posts.models import Post


class IndexView(ListView):
    template_name = 'posts/index.html'
    model = Post

class PostsView(IndexView):
    template_name = 'posts/posts.html'
    paginate_by = 6
    context_object_name = 'posts'

    #Inverter a ordem de exibição
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_post=True)
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )
        return qs


class PostDetalhes(UpdateView):
    template_name = 'posts/post_detalhes.html'
    model = Post
    form_class = FormComentario
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentario.objects.filter(publicado_comentario=True, post_comentario=post.id).order_by('-data_comentario')

        contexto['comentarios'] = comentarios
        return contexto




    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post

        if self.request.user.is_authenticated:
            comentario.autor_post_comentario = self.request.user

        comentario.save()
        messages.success(self.request, 'Comentário enviado com sucesso!')
        return redirect('post_detalhes', pk=post.id)





class PostBusca(PostsView):
    template_name = 'posts/posts_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        qs = qs.filter(
                Q(titulo_post__icontains=termo) |
                Q(categoria_post__nome_categoria__iexact=termo) |
                Q(excerto_post__icontains=termo) |
                Q(conteudo_post__icontains=termo) |
                Q(data_post__icontains=termo)
        )

        return qs
