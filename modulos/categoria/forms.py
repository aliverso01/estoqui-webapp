from .models import Categoria
from django import forms

class CategoriaForm(forms.ModelForm):
    cor = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'color',
            'class': 'form-control form-control-color',
            'title': 'Escolha a cor'
        })
    )

    class Meta:
        model = Categoria
        fields = ['nome', 'cor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-lg text-lg'}),
        }