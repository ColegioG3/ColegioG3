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
from django.urls import path
from Apps.matecomercial import views
from .views import PrimeraUnidadView, PUFraccionesView, OpeFraccionesView, ProporcionalidadView
from .views import SociedadesView, AligacionesView, AleacionesView, TantoporCientoView, PrimeraUnidadEjView
from .views import OpeFraccionesEjView, ProporcionalidadEjView, SociedadesEjView, AligacionEjView, AleacionEjView,TantoPorCientoEjView

app_name = 'matecomercial'
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('MateComercial', login_required(PrimeraUnidadView.as_view()), name='macomercialapp'),
    path('fracciones/', login_required(PUFraccionesView.as_view()), name='fraccionesapp'),
    path('OperacionesConFracciones/', login_required(OpeFraccionesView.as_view()), name='operacioesfraccionesapp'),
    path('Proporcionalidad/', login_required(ProporcionalidadView.as_view()), name='proporcionalidadapp'),
    path('Sociedades/', login_required(SociedadesView.as_view()), name='sociedadesapp'),
    path('Aligaciones/',login_required(AligacionesView.as_view()), name='aligacionesapp'),
    path('Aleaciones/',login_required(AleacionesView.as_view()), name='aleacionesapp'),
    path('TantoPorCiento/',login_required(TantoporCientoView.as_view()), name='porcientoapp'),
    path('MateComercialEjercicios', login_required(PrimeraUnidadEjView.as_view()), name='macomercialEjapp'),
    path('FraccionesEjercicios/',login_required(OpeFraccionesEjView.as_view()), name='fraccionesej'),
    path('ProporcionalidadEjercicios/',login_required(ProporcionalidadEjView.as_view()), name='proporcionalidadej'),
    path('SociedadesEjercicios/',login_required(SociedadesEjView.as_view()), name='sociedadesej'),
    path('AligacionesEjercicios/',login_required(AligacionEjView.as_view()), name='aligacionesej'),
    path('AleacionesEjercicios/',login_required(AleacionEjView.as_view()), name='aleacionesej'),
    path('TantoPorCientoEjercicios/',login_required(TantoPorCientoEjView.as_view()), name='porcientoej'),
    
]