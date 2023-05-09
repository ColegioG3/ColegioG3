from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PrimeraUnidadView(TemplateView):
    template_name='listadoUnidades.html'

class PUEcuacionesView(TemplateView):
    template_name='PrimeraUnidad/ecuaciones.html'

class PUEcuacionesSimultaneasView(TemplateView):
    template_name='PrimeraUnidad/ecuacionesSimultaneas.html'

class SUPlanoCartesianoView(TemplateView):
    template_name='SegundaUnidad/planoCartesiano.html'

class SUDistanciaView(TemplateView):
    template_name='SegundaUnidad/distancia.html'

class SUPuntoMedioView(TemplateView):
    template_name='SegundaUnidad/puntoMedio.html'

class SUPendienteView(TemplateView):
    template_name='SegundaUnidad/pendiente.html'

class SUGraficasFuncionesView(TemplateView):
    template_name='SegundaUnidad/graficaFunciones.html'

class SUPuntoYPendienteView(TemplateView):
    template_name='SegundaUnidad/puntoYPendiente.html'

class SUFuncionesLinealesYCuadraticasView(TemplateView):
    template_name='SegundaUnidad/funcionesLinealesYCuadraticas.html'

class TUTeoremaDeRectasView(TemplateView):
    template_name='TerceraUnidad/teoremaDeRectas.html'

class CUEcuacionesCirculosView(TemplateView):
    template_name='CuartaUnidad/ecuacionesCirculos.html'

