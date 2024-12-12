from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=140)
    telefone = models.CharField(max_length=12)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=200)
    data_cadastro = models.DateField()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"