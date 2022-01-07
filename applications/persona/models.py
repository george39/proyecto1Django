from django.db import models
from applications.departamento.models import Departamento, Habilidades
from ckeditor.fields import RichTextField


# Create your models here.
class Empleado(models.Model):
    # Modelo para tabla empleado
    # MUESTRA UNA LISTA DE EMPLEOS
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTROS'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('apellidos', max_length=60)
    full_name = models.CharField('Nombres completos', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidad = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()



    # INFORMACION QUE SE MUESTRA EN EL ADMINISTRADOR
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['first_name']  #['-first_name'] descendente
        unique_together = ('first_name', 'last_name') #no permite tener los dos repetidos


    def __str__(self):
        return str(self.id) + '_' + self.first_name + '_' + self.last_name