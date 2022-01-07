from django.db import models

# Create your models here.

class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()


    class Meta:
        verbose_name = 'Inicio'
        verbose_name_plural = 'Pagina de incio'
        ordering = ['titulo']  #['-titulo'] descendente
        unique_together = ('titulo', 'subtitulo') #no permite tener los dos repetidos


    def __str__(self):
        return  self.titulo
