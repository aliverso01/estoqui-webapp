from .models import Produto
from django import forms
from djmoney.forms import MoneyWidget

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        exclude = ['created_at', 'updated_at', 'user', 'preco_currency']

        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4, 'class': 'form-control form-control-lg text-lg'}),
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-lg text-lg'}),
            'preco': MoneyWidget(
                amount_widget=forms.NumberInput(attrs={
                    'class': 'form-control form-control-lg text-lg',
                    'step': '0.01',
                    'inputmode': 'decimal'
                }),
                currency_widget=forms.HiddenInput()
            ),
            'unidade': forms.Select(attrs={'class': 'form-control form-control-lg text-lg'}),
            'categoria': forms.Select(attrs={'class': 'form-control form-control-lg text-lg'}),
            'validade': forms.DateInput(attrs={'class': 'form-control form-control-lg text-lg', 'type': 'date'}, format='%Y-%m-%d'),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control form-control-lg text-lg'}),
            'estoque_minimo': forms.NumberInput(attrs={'class': 'form-control form-control-lg text-lg'}),
            'compoe_cmv': forms.CheckboxInput(attrs={'class': 'form-check-input form-check-lg'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            if self.instance and self.instance.validade:
                self.fields['validade'].input_formats = ['%Y-%m-%d']
