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
from .views import PrimeraUnidadView,PUAlgebraView,PUmonyponView,multialgebraView,divisionalgebraView,productonotableView,cocientenotableView,factorcomunView,factor2comunView

app_name = 'matematicaI'
urlpatterns = [
     path('MatematicaI', PrimeraUnidadView.as_view(), name='matematicaIapp'),
     path('Algebra/', PUAlgebraView.as_view(), name='algebraapp'),
     path('MonomioYPolinomio/', PUmonyponView.as_view(), name='monomioypolinomioapp'),
     path('MultiplicacionAlgebraica/', multialgebraView.as_view(), name='multialgebraapp'),
     path('DivisionAlgebraica/', divisionalgebraView.as_view(), name='divisionapp'),
     path('ProductosNotables/', productonotableView.as_view(), name='productoapp'),
     path('CocientesNotables/', cocientenotableView.as_view(), name='cocienteapp'),
     path('Factorizacion/', factorcomunView.as_view(), name='factorapp'),
     path('Factorizacion2/', factor2comunView.as_view(), name='factor2app'),

]
