from django.db import models
from apps.libro.models import Libro
from apps.usuario.models import Usuario
# Create your models here.

class Ejemplar(models.Model):
    codigo = models.CharField(max_length = 10)
    localizacion = models.CharField(max_length = 60)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = "autor"
        verbose_name_plural = "autores"

class Prestamo(models.Model):
    fechap = models.DateField()
    fechad = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name= "autores")
    ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE, verbose_name= "libros")        
    libro  = models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name= "libros") 