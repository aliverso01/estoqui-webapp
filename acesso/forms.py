from django import forms
from .models import Perfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['cpf', 'foto', 'whatsapp', 'dataNascimento', 'cep', 'rua', 'numero', 'bairro', 'cidade', 'estado', 'politico', 'candidato']
