from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    cpf = models.CharField(max_length=20, null=True, blank=True)
    foto = models.ImageField(upload_to='acesso/perfil/', null=True, blank=True)
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    dataNascimento= models.DateField(null=True, blank=True)
    cep = models.CharField(max_length=20, null=True, blank=True)
    rua = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)
    politico = models.BooleanField(default=False)
    candidato = models.BooleanField(default=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class Organograma(models.Model):
    funcao = models.CharField(max_length=100, null=True, blank=True)
    usuario_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True, blank=True)
    inicio = models.DateField(auto_now_add=True)
    fim = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)