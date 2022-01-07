from django import forms
from django.forms import widgets
from .models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidad'
        )
        widgets = {
            'habilidad': forms.CheckboxSelectMultiple()
        }