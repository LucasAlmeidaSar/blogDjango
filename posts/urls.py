from django.urls import path
from .views import IndexView, PostDetalhes, PostsView, PostBusca

urlpatterns = [
  path('', IndexView.as_view(), name='início'),
  path('posts/', PostsView.as_view(), name='posts'),
  path('post/<slug:slug>', PostDetalhes.as_view(), name='post_detalhes'),
  path('busca/', PostBusca.as_view(), name='post_busca'),
]