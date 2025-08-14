from django import forms
from django.forms import inlineformset_factory
from .models import FichaTecnica, Insumo

class FichaTecnicaForm(forms.ModelForm):
    class Meta:
        model = FichaTecnica
        fields = ['nome', 'descricao']  # 'user' é excluído por padrão
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-lg text-lg'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control form-control-lg text-lg', 'rows': 3}),
        }

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['produto', 'quantidade', 'unidade']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control form-control-lg text-lg'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control form-control-lg text-lg'}),
            'unidade': forms.Select(attrs={'class': 'form-control form-control-lg text-lg'}),
        }