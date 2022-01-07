from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.


admin.site.register(Habilidades)


# ME PERMITE MOSTRAR LA INFORMACION EN COLUMNAS
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name', #para mostrar una columna con nombres y apellidos
        'id'
    )

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    # filtros
    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'habilidad')
    # Este filtro solo funciona en la relacion muchos a muchos
    filter_horizontal = ('habilidad',)
admin.site.register(Empleado, EmpleadosAdmin)