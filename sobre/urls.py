from django.urls import path
from .views import Sobre

urlpatterns = [
    path('', Sobre.as_view(), name="pagina_sobre")
]