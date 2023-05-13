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

#EJERCICIOS

class PrimeraUnidadEjView(TemplateView):
    template_name='listado1unidadALEJ.html'

class PUEcuacionesLinealesEjView(TemplateView):
    template_name='PrimeraUnidadEjercicios/ecuacioneslinealesej.html'

class PUEcuacionesSegundoGradoEjView(TemplateView):
    template_name='PrimeraUnidadEjercicios/ecuacionespgdej.html'

class SUSistemasDIEjView(TemplateView):
    template_name='SegundaUnidadEjercicios/sistemadosiej.html'

class SUDeterminacionDTEjView(TemplateView):
    template_name='SegundaUnidadEjercicios/determinaciondtej.html'

class SUReglaCramerEjView(TemplateView):
    template_name='SegundaUnidadEjercicios/reglacramerej.html'

class SUProblemasdtiEjView(TemplateView):
    template_name='SegundaUnidadEjercicios/problemasdtiej.html'

class TUMatricesEjView(TemplateView):
    template_name='TerceraUnidadEjercicios/matricesej.html'

class TUMenorCofactorEjView(TemplateView):
    template_name='TerceraUnidadEjercicios/menorycofactorej.html'

class TUGaussianaEjView(TemplateView):
    template_name='TerceraUnidadEjercicios/gaussianaej.html'

class TUGaussJordanEjView(TemplateView):
    template_name='TerceraUnidadEjercicios/gaussjordanej.html'

class CUVectoresEjView(TemplateView):
    template_name='CuartaUnidadEjercicios/vectoresej.html'

class CUPlanoEjView(TemplateView):
    template_name='CuartaUnidadEjercicios/planocartesianoej.html'

class CUDeterminantesEjView(TemplateView):
    template_name='CuartaUnidadEjercicios/determinantesej.html'