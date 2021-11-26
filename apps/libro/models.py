from django.db import models
from apps.autor.models import Autor
# Create your models here.

class Libro(models.Model):
    codigo = models.IntegerField()
    titulo = models.CharField(max_length = 40)
    isbn = models.CharField(max_length = 10)
    editorial = models.CharField(max_length = 20)
    numeropagina = models.IntegerField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "libro"
        verbose_name_plural = "libros"


class AutorLibro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name= "autores")
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name= "libros")