from django.urls import path
from .views import lista_categorias, create_categoria, edit_categoria, delete_categoria

urlpatterns = [
    path('', lista_categorias, name='lista_categorias'),
    path('criar/', create_categoria, name='create_categoria'),
    path('editar/<int:id>/', edit_categoria, name='edit_categoria'),
    path('deletar/<int:id>/', delete_categoria, name='delete_categoria'),
]