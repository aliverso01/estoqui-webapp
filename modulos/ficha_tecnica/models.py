from django.db import models
from modulos.produto.models import Produto
from django.contrib.auth.models import User

# Create your models here.
class FichaTecnica(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    insumos = models.ManyToManyField(Produto, related_name='fichas_tecnicas')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)