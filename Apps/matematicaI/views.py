from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PrimeraUnidadView(TemplateView):
    template_name='listado1unidadmate.html'

class PrimeraUnidadejerView(TemplateView):
    template_name='listado1unidadmateejer.html'

class PUAlgebraView(TemplateView):
    template_name='PrimeraUnidad/algebra.html'

class algebraejerView(TemplateView):
    template_name='PrimeraUnidadEjercicios/algebraejercicios.html'

class PUmonyponView(TemplateView):
    template_name='PrimeraUnidad/monomioypolinomio.html'

class monejView(TemplateView):
    template_name='PrimeraUnidadEjercicios/monomioypolinomioej.html'

  

class multialgebraView(TemplateView):
    template_name='SegundaUnidad/multialgebra.html'

class multialgebraejerView(TemplateView):
    template_name='SegundaUnidadEjercicios/multiplicacioneje.html'

   

class divisionalgebraView(TemplateView):
    template_name='SegundaUnidad/divisionalgebra.html'

class divisionalgebraejerView(TemplateView):
    template_name='SegundaUnidadEjercicios/Divisioneje.html'


class productonotableView(TemplateView):
    template_name='TerceraUnidad/productosnotables.html'

class productonotableejerView(TemplateView):
    template_name='TerceraUnidadEjercicios/productosnotablesejer.html'

  

class cocientenotableView(TemplateView):
    template_name='TerceraUnidad/cocientenotable.html'

class cocientenotableejerView(TemplateView):
    template_name='TerceraUnidadEjercicios/cocientenotableejer.html'

    

class factorcomunView(TemplateView):
    template_name='CuartaUnidad/factorcomun.html'


class factorcomunejerView(TemplateView):
    template_name='CuartaUnidadEjercicios/factorcomunejer.html'
    

class factor2comunView(TemplateView):
    template_name='CuartaUnidad/factor2.html'

class factor2comunejerView(TemplateView):
    template_name='CuartaUnidadEjercicios/factorcomun2ejer.html'

    
