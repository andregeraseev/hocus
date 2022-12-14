from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    celular = models.CharField(max_length=12)

    def __str__(self):
        return str(self.usuario)

class UsuarioSemRegistro(models.Model):
    usuario_sem_registro = models.CharField(max_length=50)
    cpf_sem_registro = models.CharField(max_length=11)
    celular_sem_registro = models.CharField(max_length=12)

    def __str__(self):
        return str(self.usuario_sem_registro)