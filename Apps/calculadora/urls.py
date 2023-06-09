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
from Apps.calculadora import views
from .views import CalculadoraView,HerramientasView

app_name = 'calculadora'
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('Calculadora', login_required(CalculadoraView.as_view()), name='calculadoraapp'),
    path('OtrasHerramientas', login_required(HerramientasView.as_view()), name='herramientasaapp')
    
]