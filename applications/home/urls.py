from django.contrib import admin
from django.urls import path



from . import views



urlpatterns = [
    path('home/', views.PruebaView.as_view()),
    path('list/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view()),
    path('create/', views.PruebaCreateView.as_view(), name='prueba_add')
]