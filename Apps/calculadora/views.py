from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CalculadoraView(TemplateView):
    template_name='calculadora.html'

class HerramientasView(TemplateView):
    template_name='herramientas.html'