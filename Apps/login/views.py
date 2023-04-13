from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class LoginView(TemplateView):
    template_name='index.html'

class HomeView(TemplateView):
    template_name='home.html'

class PrimeraUnidadView(TemplateView):
    template_name='PrimeraUnidad/listado1unidad.html'

class PUFraccionesView(TemplateView):
    template_name='PrimeraUnidad/fracciones.html'