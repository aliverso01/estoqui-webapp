from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
