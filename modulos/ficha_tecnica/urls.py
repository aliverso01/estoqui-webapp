from django import urls
from .views import lista_fichas_tecnicas, create_ficha_tecnica, edit_ficha_tecnica, delete_ficha_tecnica, add_insumo, edit_insumo, delete_insumo

urlpatterns = [
    urls.path('', lista_fichas_tecnicas, name='lista_fichas_tecnicas'),
    urls.path('nova/', create_ficha_tecnica, name='create_ficha_tecnica'),
    urls.path('editar/<int:id>/', edit_ficha_tecnica, name='edit_ficha_tecnica'),
    urls.path('deletar/<int:id>/', delete_ficha_tecnica, name='delete_ficha_tecnica'),
    
    # Rotas para adicionar insumos
    urls.path('<int:ficha_id>/adicionar_insumo/', add_insumo, name='add_insumo'),
    urls.path('<int:ficha_id>/editar_insumo/<int:insumo_id>/', edit_insumo, name='edit_insumo'),
    urls.path('<int:ficha_id>/deletar_insumo/<int:insumo_id>/', delete_insumo, name='delete_insumo'),
]