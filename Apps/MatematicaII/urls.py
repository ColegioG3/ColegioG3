"""
URL configuration for ColegioG3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Apps.MatematicaII import views
from .views import ( DistanciaEjerciciosView, EcuacionesEjerciciosView, EcuacionesSimultaneasEjerciciosView, FormaPuntoEjerciciosView, FuncionesLinealesCEjerciciosView, GraficosEjerciciosView, PendienteEjerciciosView, PlanoCartesianoEjerciciosView, 
            PrimeraUnidadEjerciciosView, PrimeraUnidadView, PUEcuacionesView, 
            PUEcuacionesSimultaneasView, PuntoMedioEjerciciosView, SUPlanoCartesianoView, SUDistanciaView, SUPuntoMedioView, SUPendienteView, SUGraficasFuncionesView, 
            SUPuntoYPendienteView, SUFuncionesLinealesYCuadraticasView, TUTeoremaDeRectasView, CUEcuacionesCirculosView, EcuacionesCirculosEjerciciosView, TeoremaDeRectasView)


app_name = 'MatematicaII'

urlpatterns = [
   path('MatematicaII', PrimeraUnidadView.as_view(), name='matematicaiiapp'),
   path('ecuaciones/', PUEcuacionesView.as_view(), name='ecuacionesapp'),
   path('ecuacionesSimultaneas/', PUEcuacionesSimultaneasView.as_view(), name='ecuacionesSimultaneasapp'),
   path('planoCartesiano/', SUPlanoCartesianoView.as_view(), name='planoCartesianoapp'),
   path('distancia/', SUDistanciaView.as_view(), name='distanciaapp'),
   path('puntoMedio/', SUPuntoMedioView.as_view(), name='puntoMedioapp'),
   path('pendiente/', SUPendienteView.as_view(), name='pendienteapp'),
   path('graficas/', SUGraficasFuncionesView.as_view(), name='graficaFuncionesapp'),
   path('puntoPendiente/', SUPuntoYPendienteView.as_view(), name='puntoPendienteapp'),
   path('funcionesLinealesyC/', SUFuncionesLinealesYCuadraticasView.as_view(), name='funcionesLinealesyCapp'),
   path('teoremaRectas/', TUTeoremaDeRectasView.as_view(), name='teoremaRectasapp'),
   path('ecuacionesCirculos/', CUEcuacionesCirculosView.as_view(), name='ecuacionesCirculosapp'),
   path('matematicaIIEjercicios/', PrimeraUnidadEjerciciosView.as_view(), name='matematicaIIEjerciciosapp'),
   path('ecuacionesEjercicios/', EcuacionesEjerciciosView.as_view(), name='ecuacionesEjercicios'),
   path('ecuacionesSimultaneasEjercicios/', EcuacionesSimultaneasEjerciciosView.as_view(), name='ecuacionesSimultaneasEjercicios'),
   path('planoCartesianoEjercicios/', PlanoCartesianoEjerciciosView.as_view(), name='planoCartesianoEjercicios'),
   path('distanciaEjercicios/', DistanciaEjerciciosView.as_view(), name='distanciaEjercicios'),
   path('puntoMedioEjercicios/', PuntoMedioEjerciciosView.as_view(), name='puntoMedioEjercicios'),
   path('pendienteEjercicios/', PendienteEjerciciosView.as_view(), name='pendienteEjercicios'),
   path('graficasFuncionesEjercicios/', GraficosEjerciciosView.as_view(), name='graficasFuncionesEjercicios'),
   path('formaPuntoEjercicios/', FormaPuntoEjerciciosView.as_view(), name='formaPuntoEjercicios'),
   path('FuncionesEjercicios/', FuncionesLinealesCEjerciciosView.as_view(), name='FuncionesEjercicios'),
   path('ecuacionesCirculosEjercicios/', EcuacionesCirculosEjerciciosView.as_view(), name='ecuacionesCirculosEjercicios'),
   path('teoremasRectasEjercicios/', TeoremaDeRectasView.as_view(), name='teoremasRectasEjercicios'),
]