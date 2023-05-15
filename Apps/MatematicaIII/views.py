from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ListadoMIIIView(TemplateView):
    template_name='listado1unidadMIII.html'

class SUTeoremasLMIIIView(TemplateView):
    template_name='SegundaUnidad/teoremaslimites.html'

class SULimitesInfinitoView(TemplateView):
    template_name='SegundaUnidad/limitesinfinito.html'

class TUConstantesView(TemplateView):
    template_name='TerceraUnidad/constantes.html'

class TUPotenciaView(TemplateView):
    template_name='TerceraUnidad/reglapotencia.html'

class TUTeoremasDerivacionView(TemplateView):
    template_name='TerceraUnidad/teoremasderivacion.html'

class PUTeoremaDeRectasView(TemplateView):
    template_name='PrimeraUnidad/TeoremaDeRectas.html'

class PUecuacionCirculoView(TemplateView):
    template_name='PrimeraUnidad/ecuacionCirculo.html'

class PUcomplementoCuadradosView(TemplateView):
    template_name='PrimeraUnidad/complementoCuadrados.html'

#Ejercicios
class ListadoMIIIEjView(TemplateView):
    template_name='listado1unidadMIIIEj.html'

class SUTeoremasLMIIIEjView(TemplateView):
    template_name='SegundaUnidadEjercicios/teoremaslimitesej.html'

class SULimitesInfinitoEjView(TemplateView):
    template_name='SegundaUnidadEjercicios/limitesinfinitoej.html'

class TUConstantesEjView(TemplateView):
    template_name='TerceraUnidadEjercicios/constantesej.html'

class TUPotenciaEjView(TemplateView):
    template_name='TerceraUnidadEjercicios/reglapotenciaej.html'

class TUTeoremasDerivacionEjView(TemplateView):
    template_name='TerceraUnidadEjercicios/teoremasderivacionej.html'