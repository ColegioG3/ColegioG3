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
from .views import PrimeraUnidadView, PUEcuacionesLinealesView, PUEcuacionesSegundoGradoView, SUSistemasDIView, SUDeterminacionDTView, SUReglaCramerView, SUProblemasdtiView, TUMatricesView, TUMenorCofactorView, TUGaussianaView, TUGaussJordanView, CUVectoresView, CUPlanoView, CUDeterminantesView, PrimeraUnidadEjView, PUEcuacionesLinealesEjView, PUEcuacionesSegundoGradoEjView, SUDeterminacionDTEjView, SUProblemasdtiEjView, SUReglaCramerEjView, SUSistemasDIEjView, TUGaussianaEjView, TUGaussJordanEjView, TUMatricesEjView, TUMenorCofactorEjView, CUDeterminantesEjView, CUPlanoEjView, CUVectoresEjView

app_name = 'AlgebraComercial'

urlpatterns = [
    path('algebralineal', PrimeraUnidadView.as_view(), name='algebralinealapp'),
    path('ecuacioneslineales/', PUEcuacionesLinealesView.as_view(), name='ecuacioneslapp'),
    path('ecuacionesprimergradodosincognitas/', PUEcuacionesSegundoGradoView.as_view(), name='ecuacionespgdapp'),
    path('sistemasdosi/', SUSistemasDIView.as_view(), name='sistemasdosiapp'),
    path('determinaciondt/', SUDeterminacionDTView.as_view(), name='determinaciondtapp'),
    path('regladecramer/', SUReglaCramerView.as_view(), name='reglacramerapp'),
    path('problemasdosytresincgonitas/', SUProblemasdtiView.as_view(), name='problemasdtiapp'),
    path('matrices/', TUMatricesView.as_view(), name='matricesapp'),
    path('menorycofactor/', TUMenorCofactorView.as_view(), name='menorcofactorapp'),
    path('eliminaciongaussiana/', TUGaussianaView.as_view(), name='gaussianaapp'),
    path('eliminaciongaussjordan/', TUGaussJordanView.as_view(), name='gaussjordanapp'),
    path('vectores/', CUVectoresView.as_view(), name='vectoresapp'),
    path('planocartesiano/', CUPlanoView.as_view(), name='planoapp'),
    path('determinantes/', CUDeterminantesView.as_view(), name='determinantesapp'),
    # EJERCICIOS
    path('algebralinealejercicios', PrimeraUnidadEjView.as_view(), name='algebralinealEjapp'),
    path('ecuacioneslinealesejercicios/', PUEcuacionesLinealesEjView.as_view(), name='ecuacioneslejapp'),
    path('ecuacionesprimergradoejercicios/', PUEcuacionesSegundoGradoEjView.as_view(), name='ecuacionespgdejapp'),
    path('sistemasdosiejercicios/', SUSistemasDIEjView.as_view(), name='sistemasdosiejapp'),
    path('determinaciondtejercicios/', SUDeterminacionDTEjView.as_view(), name='determinaciondtejapp'),
    path('regladecramerejercicios/', SUReglaCramerEjView.as_view(), name='reglacramerejapp'),
    path('problemasdosytresincgonitasejercicios/', SUProblemasdtiEjView.as_view(), name='problemasdtiejapp'),
    path('matricesejercicios/', TUMatricesEjView.as_view(), name='matricesejapp'),
    path('menorycofactorejercicios/', TUMenorCofactorEjView.as_view(), name='menorcofactorejapp'),
    path('eliminaciongaussianaejercicios/', TUGaussianaEjView.as_view(), name='gaussianaejapp'),
    path('eliminaciongaussjordanejercicios/', TUGaussJordanEjView.as_view(), name='gaussjordanejapp'),
    path('vectoresejercicios/', CUVectoresEjView.as_view(), name='vectoresejapp'),
    path('planocartesianoejercicios/', CUPlanoEjView.as_view(), name='planoejapp'),
    path('determinantesejercicios/', CUDeterminantesEjView.as_view(), name='determinantesejapp'),
]