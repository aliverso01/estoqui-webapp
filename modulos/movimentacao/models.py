from django.db import models
from modulos.produto.models import Produto
from django.contrib.auth.models import User

# Create your models here.
class Movimentacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    tipo = models.CharField(max_length=10, 
                            choices=[('entrada', 'Entrada'), 
                                     ('saida', 'Saída')])
    origem = models.CharField(max_length=100, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.produto.nome} ({self.quantidade})"