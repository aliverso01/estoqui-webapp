from django.db import models
from modulos.produto.models import Produto
from modulos.unidade.models import Unidade
from django.contrib.auth.models import User



class Insumo(models.Model):
    ficha_tecnica = models.ForeignKey('FichaTecnica', on_delete=models.CASCADE, related_name='insumos')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='insumos')
    quantidade = models.DecimalField(max_digits=10, decimal_places=3)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name='insumos')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} {self.unidade.sigla}"


class FichaTecnica(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome