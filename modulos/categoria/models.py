from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cor = ColorField(default='blue')

    def produtos_count(self):
        return self.produtos.count()

    def __str__(self):
        return self.nome