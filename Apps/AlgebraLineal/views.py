from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PrimeraUnidadView(TemplateView):
    template_name='listado1unidad.html'

class PUFraccionesView(TemplateView):
    template_name='PrimeraUnidad/fracciones.html'