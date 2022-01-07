from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView

# importar los modelos
from .models import Prueba

from .forms import PruebaForm


class PruebaView(TemplateView):
    template_name = 'home/prueba.html'



class PruebaListView(ListView):
    template_name = 'home/list.html'
    context_object_name = 'ListaNumeros'
    queryset = ['1', '10', ' 20', '30']




class ListarPrueba(ListView):
    template_name = 'home/listar_prueba.html' 
    model = Prueba
    context_object_name = 'lista' 




class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = Prueba  
    form_class = PruebaForm  
    success_url = '/'   