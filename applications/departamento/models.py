from django.db import models

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)


    class Meta:
        verbose_name = 'Hbilidad'
        verbose_name_plural = 'Hbilidades empleados'


    def __str__(self):
        return str(self.id) + '-' + self.habilidad   



class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre corto', max_length=50)
    anulate = models.BooleanField('Anulado', default=False)



    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Area de la empresa'
        ordering = ['name']  #['-name'] descendente
        unique_together = ('name', 'shor_name') #no permite tener los dos repetidos


    def __str__(self):
        return self.name + '-' + self.shor_name