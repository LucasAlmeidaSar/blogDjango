from django.urls import path
from .views import contatoView

urlpatterns = [
    path('', contatoView, name='pagina_contato')
]