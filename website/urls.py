from django.urls import path
from . import views
from .views import enviar_email

urlpatterns = [
    path('', views.website, name='home'),
    # outras URLs do seu aplicativo podem ser adicionadas aqui
    path('enviar_email/', enviar_email, name='enviar_email'),
    
]
