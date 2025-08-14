from django.urls import path
from .views import lista_produtos, create_produto, edit_produto, delete_produto

urlpatterns = [
    path('lista/', lista_produtos, name='lista_produtos'),
    path('criar/', create_produto, name='create_produto'),
    path('editar/<int:id>/', edit_produto, name='edit_produto'),
    path('deletar/<int:id>/', delete_produto, name='delete_produto'),
]