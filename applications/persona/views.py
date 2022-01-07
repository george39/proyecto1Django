from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.
from .models import Empleado
from .forms import EmpleadoForm

# PROYECOT 1
class InicioView(TemplateView):
    template_name = 'home/inicio.html'


'''
REQUERIMIENTOS 
1. Listar todos los empleados de la empresa
2. listar todos los empleados que pertenecen a un area de la empresa
3. listar empleados por trabajo
4. listar empleados por palabra clave
5. listar habilidades de un empleado
'''

# listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4   # paginacion
    

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave   # icontains busca similitudes en las cadenas 
        )
        return lista



# listar todos los empleados que pertenecen a un area de la empresa
class ListByAreaEpleado(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name = area
        ) 

        return lista



class ListEpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    context_object_name = 'empleados'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

    


# LISTAR EMPLEADOS POR PALABRA CLAVE  --- de los filtros mas utilizados
class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'   #para acceder mejor desde el html con el nombre de empleados


    # Esta funcion es de django
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista



# LISTAR EMPLEADOS POR HABILIDADES
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'


    def get_queryset(self):
        empleado = Empleado.objects.get(id=4)
        return empleado.habilidad.all() 




# DELLES DEL EMPLEADO
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail_empleado.html' 


    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes' 
        return context            



class SuccessView(TemplateView):
    template_name = 'persona/success.html'


# VISTA PARA CREAR REGISTROS EN BD
class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'  
    model = Empleado 
    form_class = EmpleadoForm
    success_url =  reverse_lazy('persona_app:empleados_admin')     #'.' para que se recargue la url en la misma pagina   


    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)




#  ACTUALIZAR UN USUARIO
class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        
        'habilidad',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')



# ELIMINAR UN EMPLEADO
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona_app:empleados_admin')    