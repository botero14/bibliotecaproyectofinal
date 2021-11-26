from django.db import models
# Create your models here.

class Usuario(models.Model):
    codigo = models.CharField(max_length = 10)
    nombre = models.CharField(max_length = 60)
    direccion = models.CharField(max_length = 30)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
