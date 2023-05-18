from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PrimeraUnidadView(TemplateView):
    template_name='listado1unidad.html'

class PUFraccionesView(TemplateView):
    template_name='PrimeraUnidad/fracciones.html'

class OpeFraccionesView(TemplateView):
    template_name='PrimeraUnidad/OperacionesConFracciones.html'

class ProporcionalidadView(TemplateView):
    template_name='SegundaUnidad/proporcionalidad.html'

class SociedadesView(TemplateView):
    template_name='TerceraUnidad/ReglaSociedades.html'

class AligacionesView(TemplateView):
    template_name='TerceraUnidad/Aligacion.html'

class AleacionesView(TemplateView):
    template_name='TerceraUnidad/Aleaciones.html'

class TantoporCientoView(TemplateView):
    template_name='TerceraUnidad/TantoPorCiento.html'

class PrimeraUnidadEjView(TemplateView):
    template_name='listado1unidadEj.html'

class OpeFraccionesEjView(TemplateView):
    template_name='PrimeraUnidadEjercicios/OperacionesConFraccionesEj.html'

class ProporcionalidadEjView(TemplateView):
    template_name='SegundaUnidadEjercicio/proporcionalidadEj.html'

class SociedadesEjView(TemplateView):
    template_name='TerceraUnidadEjercicios/ReglaSociedadesEj.html'

class AligacionEjView(TemplateView):
    template_name='TerceraUnidadEjercicios/AligacionEj.html'

class AleacionEjView(TemplateView):
    template_name='TerceraUnidadEjercicios/AleacionesEj.html'

class TantoPorCientoEjView(TemplateView):
    template_name='TerceraUnidadEjercicios/TantoPorCientoEj.html'