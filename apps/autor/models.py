from django.db import models
# Create your models here.

class Autor(models.Model):
    codigo = models.CharField(max_length = 60)
    nombre = models.CharField(max_length = 60)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
