from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PrimeraUnidadView(TemplateView):
    template_name='listado1unidadAL.html'

class PUEcuacionesLinealesView(TemplateView):
    template_name='PrimeraUnidad/ecuacioneslineales.html'

class PUEcuacionesSegundoGradoView(TemplateView):
    template_name='PrimeraUnidad/ecuacionespgd.html'

class SUSistemasDIView(TemplateView):
    template_name='SegundaUnidad/sistemasdosi.html'

class SUDeterminacionDTView(TemplateView):
    template_name='SegundaUnidad/determinaciondt.html'

class SUReglaCramerView(TemplateView):
    template_name='SegundaUnidad/reglacramer.html'

class SUProblemasdtiView(TemplateView):
    template_name='SegundaUnidad/problemasdti.html'

class TUMatricesView(TemplateView):
    template_name='TerceraUnidad/matrices.html'

class TUMenorCofactorView(TemplateView):
    template_name='TerceraUnidad/menorycofactor.html'

class TUGaussianaView(TemplateView):
    template_name='TerceraUnidad/gaussiana.html'

class TUGaussJordanView(TemplateView):
    template_name='TerceraUnidad/gaussjordan.html'

class CUVectoresView(TemplateView):
    template_name='CuartaUnidad/vectores.html'

class CUPlanoView(TemplateView):
    template_name='CuartaUnidad/planocartesiano.html'

class CUDeterminantesView(TemplateView):
    template_name='CuartaUnidad/determinantes.html'

