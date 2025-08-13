from django.urls import path
from .views import PerfilView

urlpatterns = [
    path('perfil/', PerfilView.as_view(), name='perfil'),
    # outras URLs do aplicativo "acesso" podem ser adicionadas aqui...
]