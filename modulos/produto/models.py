from django.db import models
from modulos.categoria.models import Categoria
from modulos.unidade.models import Unidade
from django.contrib.auth.models import User

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True, related_name='produtos')
    validade = models.DateField()
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, null=True, blank=True)
    quantidade = models.IntegerField()
    estoque_minimo = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    compoe_cmv = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome



# Importante ressaltar para a composição do CMV:
# - O campo "compoe_cmv" deve ser marcado como True para os produtos que compõem o CMV.
# - O que compoe o CMV é o produto que vai para a venda. Insumos não entram nessa composição.
# - A ficha técnica do produto deve conter todos os insumos necessários para a produção do item.