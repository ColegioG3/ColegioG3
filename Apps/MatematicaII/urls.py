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
from django.contrib.auth.decorators import login_required
urlpatterns = [
   path('MatematicaII', login_required(PrimeraUnidadView.as_view()), name='matematicaiiapp'),
   path('ecuaciones/', login_required(PUEcuacionesView.as_view()), name='ecuacionesapp'),
   path('ecuacionesSimultaneas/', login_required(PUEcuacionesSimultaneasView.as_view()), name='ecuacionesSimultaneasapp'),
   path('planoCartesiano/', login_required(SUPlanoCartesianoView.as_view()), name='planoCartesianoapp'),
   path('distancia/', login_required(SUDistanciaView.as_view()), name='distanciaapp'),
   path('puntoMedio/', login_required(SUPuntoMedioView.as_view()), name='puntoMedioapp'),
   path('pendiente/', login_required(SUPendienteView.as_view()), name='pendienteapp'),
   path('graficas/', login_required(SUGraficasFuncionesView.as_view()), name='graficaFuncionesapp'),
   path('puntoPendiente/', login_required(SUPuntoYPendienteView.as_view()), name='puntoPendienteapp'),
   path('funcionesLinealesyC/', login_required(SUFuncionesLinealesYCuadraticasView.as_view()), name='funcionesLinealesyCapp'),
   path('teoremaRectas/', login_required(TUTeoremaDeRectasView.as_view()), name='teoremaRectasapp'),
   path('ecuacionesCirculos/', login_required(CUEcuacionesCirculosView.as_view()), name='ecuacionesCirculosapp'),
   path('matematicaIIEjercicios/', login_required(PrimeraUnidadEjerciciosView.as_view()), name='matematicaIIEjerciciosapp'),
   path('ecuacionesEjercicios/', login_required(EcuacionesEjerciciosView.as_view()), name='ecuacionesEjercicios'),
   path('ecuacionesSimultaneasEjercicios/', login_required(EcuacionesSimultaneasEjerciciosView.as_view()), name='ecuacionesSimultaneasEjercicios'),
   path('planoCartesianoEjercicios/', login_required(PlanoCartesianoEjerciciosView.as_view()), name='planoCartesianoEjercicios'),
   path('distanciaEjercicios/', login_required(DistanciaEjerciciosView.as_view()), name='distanciaEjercicios'),
   path('puntoMedioEjercicios/', login_required(PuntoMedioEjerciciosView.as_view()), name='puntoMedioEjercicios'),
   path('pendienteEjercicios/', login_required(PendienteEjerciciosView.as_view()), name='pendienteEjercicios'),
   path('graficasFuncionesEjercicios/', login_required(GraficosEjerciciosView.as_view()), name='graficasFuncionesEjercicios'),
   path('formaPuntoEjercicios/', login_required(FormaPuntoEjerciciosView.as_view()), name='formaPuntoEjercicios'),
   path('FuncionesEjercicios/', login_required(FuncionesLinealesCEjerciciosView.as_view()), name='FuncionesEjercicios'),
   path('ecuacionesCirculosEjercicios/', login_required(EcuacionesCirculosEjerciciosView.as_view()), name='ecuacionesCirculosEjercicios'),
   path('teoremasRectasEjercicios/', login_required(TeoremaDeRectasView.as_view()), name='teoremasRectasEjercicios'),
]