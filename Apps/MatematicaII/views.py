from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PrimeraUnidadView(TemplateView):
    template_name='listadoUnidades.html'

class PUEcuacionesView(TemplateView):
    template_name='PrimeraUnidad/ecuaciones.html'