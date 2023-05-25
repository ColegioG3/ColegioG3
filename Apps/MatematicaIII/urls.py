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
from Apps.AlgebraLineal import views
from .views import ListadoMIIIView, SUTeoremasLMIIIView, SULimitesInfinitoView, TUConstantesView, TUPotenciaView, TUTeoremasDerivacionView, PUTeoremaDeRectasView, PUecuacionCirculoView, PUcomplementoCuadradosView, SULimitesInfinitoEjView,SUTeoremasLMIIIEjView, ListadoMIIIEjView, TUConstantesEjView, TUPotenciaEjView, TUTeoremasDerivacionEjView, PUcomplementoCuadradosEjView, PUecuacionCirculoEjView, PUTeoremaDeRectasEjView

app_name = 'MatematicaIII'
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('matematicaIII', login_required(ListadoMIIIView.as_view()), name='matematicaIIIapp'),
    path('teoremaslimites', login_required(SUTeoremasLMIIIView.as_view()), name='teoremasLapp'),
    path('limitesinfinitos', login_required(SULimitesInfinitoView.as_view()), name='limitesIapp'),
    path('reglasconstantes', login_required(TUConstantesView.as_view()), name='constantesapp'),
    path('reglaspotencia', login_required(TUPotenciaView.as_view()), name='potenciaapp'),
    path('teoremasderivacion', login_required(TUTeoremasDerivacionView.as_view()), name='teoremasderivacionapp'),
    path('teoremasderectas', login_required(PUTeoremaDeRectasView.as_view()), name='teoremasderectasapp'),
    path('ecuacioncirculo', login_required(PUecuacionCirculoView.as_view()), name='circuloapp'),
    path('complementoscuadrados', login_required(PUcomplementoCuadradosView.as_view()), name='complementosapp'),
    #Ejercicios
    path('matematicaIIIejercicios', login_required(ListadoMIIIEjView.as_view()), name='matematicaIIIEjapp'),
    path('teoremaslimitesejercicios', login_required(SUTeoremasLMIIIEjView.as_view()), name='teoremasLEjapp'),
    path('limitesinfinitosejercicios', login_required(SULimitesInfinitoEjView.as_view()), name='limitesIEjapp'),
    path('reglasconstantesejercicios', login_required(TUConstantesEjView.as_view()), name='constantesEjapp'),
    path('reglaspotenciaejercicios', login_required(TUPotenciaEjView.as_view()), name='potenciaEjapp'),
    path('teoremasderivacionejercicios', login_required(TUTeoremasDerivacionEjView.as_view()), name='teoremasderivacionEjapp'),
    path('teoremasderectasejercicios', login_required(PUTeoremaDeRectasEjView.as_view()), name='teoremasderectasEjapp'),
    path('ecuacioncirculoejercicios', login_required(PUecuacionCirculoEjView.as_view()), name='circuloEjapp'),
    path('complementoscuadradosejercicios', login_required(PUcomplementoCuadradosEjView.as_view()), name='complementosEjapp'),
]