from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PrimeraUnidadView(TemplateView):
    template_name='listado1unidadmate.html'

class PUAlgebraView(TemplateView):
    template_name='PrimeraUnidad/algebra.html'

class PUmonyponView(TemplateView):
    template_name='PrimeraUnidad/monomioypolinomio.html'

class multialgebraView(TemplateView):
    template_name='SegundaUnidad/multialgebra.html'

class divisionalgebraView(TemplateView):
    template_name='SegundaUnidad/divisionalgebra.html'

class productonotableView(TemplateView):
    template_name='TerceraUnidad/productosnotables.html'

class cocientenotableView(TemplateView):
    template_name='TerceraUnidad/cocientenotable.html'

class factorcomunView(TemplateView):
    template_name='CuartaUnidad/factorcomun.html'

class factor2comunView(TemplateView):
    template_name='CuartaUnidad/factor2.html'
