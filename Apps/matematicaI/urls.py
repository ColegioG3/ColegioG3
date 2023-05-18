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
from Apps.matematicaI import views
from .views import PrimeraUnidadView,PUAlgebraView,PUmonyponView,multialgebraView,divisionalgebraView,productonotableView,cocientenotableView,factorcomunView,factor2comunView,PrimeraUnidadView
from .views import PrimeraUnidadejerView,algebraejerView,monejView,multialgebraejerView,divisionalgebraejerView
from .views import productonotableejerView,cocientenotableejerView,factorcomunejerView,factor2comunejerView
app_name = 'matematicaI'
urlpatterns = [
     path('MatematicaI', PrimeraUnidadView.as_view(), name='matematicaIapp'),
     path('matematicaIejer', PrimeraUnidadejerView.as_view(), name='matematicaejerIapp'),
     path('Algebra/', PUAlgebraView.as_view(), name='algebraapp'),
     path('EjerciciosAlgebra/', algebraejerView.as_view(), name='ejerciciosalgebraapp'),
     path('MonomioYPolinomio/', PUmonyponView.as_view(), name='monomioypolinomioapp'),
     path('EjerciciosMonomioYPolinomio/', monejView.as_view(), name='ejermonomioypolinomioapp'),
     path('MultiplicacionAlgebraica/', multialgebraView.as_view(), name='multialgebraapp'),
     path('MultiplicacionAlgebraicaEjercicios/', multialgebraejerView.as_view(), name='ejermultialgebraapp'),
     path('DivisionAlgebraica/', divisionalgebraView.as_view(), name='divisionapp'),
     path('DivisionAlgebraicaEjercicios/', divisionalgebraejerView.as_view(), name='ejerdivisionapp'),
     path('ProductosNotables/', productonotableView.as_view(), name='productoapp'),
     path('ProductosNotablesEjercicios/', productonotableejerView.as_view(), name='productoejerapp'),
     path('CocientesNotables/', cocientenotableView.as_view(), name='cocienteapp'),
     path('CocientesNotablesEjercicios/', cocientenotableejerView.as_view(), name='ejercocienteapp'),
     path('Factorizacion/', factorcomunView.as_view(), name='factorapp'),
     path('FactorizacionEjercicios/', factorcomunejerView.as_view(), name='ejerfactorapp'),
     path('Factorizacion2/', factor2comunView.as_view(), name='factor2app'),
     path('Factorizacion2Ejercicios/', factor2comunejerView.as_view(), name='ejerfactor2app'),
]
