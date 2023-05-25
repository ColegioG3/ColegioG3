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
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('algebralineal', login_required(PrimeraUnidadView.as_view()), name='algebralinealapp'),
    path('ecuacioneslineales/', login_required(PUEcuacionesLinealesView.as_view()), name='ecuacioneslapp'),
    path('ecuacionesprimergradodosincognitas/', login_required(PUEcuacionesSegundoGradoView.as_view()), name='ecuacionespgdapp'),
    path('sistemasdosi/', login_required(SUSistemasDIView.as_view()), name='sistemasdosiapp'),
    path('determinaciondt/', login_required(SUDeterminacionDTView.as_view()), name='determinaciondtapp'),
    path('regladecramer/', login_required(SUReglaCramerView.as_view()), name='reglacramerapp'),
    path('problemasdosytresincgonitas/', login_required(SUProblemasdtiView.as_view()), name='problemasdtiapp'),
    path('matrices/', login_required(TUMatricesView.as_view()), name='matricesapp'),
    path('menorycofactor/', login_required(TUMenorCofactorView.as_view()), name='menorcofactorapp'),
    path('eliminaciongaussiana/', login_required(TUGaussianaView.as_view()), name='gaussianaapp'),
    path('eliminaciongaussjordan/', login_required(TUGaussJordanView.as_view()), name='gaussjordanapp'),
    path('vectores/', login_required(CUVectoresView.as_view()), name='vectoresapp'),
    path('planocartesiano/', login_required(CUPlanoView.as_view()), name='planoapp'),
    path('determinantes/', login_required(CUDeterminantesView.as_view()), name='determinantesapp'),
    # EJERCICIOS
    path('algebralinealejercicios', login_required(PrimeraUnidadEjView.as_view()), name='algebralinealEjapp'),
    path('ecuacioneslinealesejercicios/', login_required(PUEcuacionesLinealesEjView.as_view()), name='ecuacioneslejapp'),
    path('ecuacionesprimergradoejercicios/', login_required(PUEcuacionesSegundoGradoEjView.as_view()), name='ecuacionespgdejapp'),
    path('sistemasdosiejercicios/', login_required(SUSistemasDIEjView.as_view()), name='sistemasdosiejapp'),
    path('determinaciondtejercicios/', login_required(SUDeterminacionDTEjView.as_view()), name='determinaciondtejapp'),
    path('regladecramerejercicios/', login_required(SUReglaCramerEjView.as_view()), name='reglacramerejapp'),
    path('problemasdosytresincgonitasejercicios/', login_required(SUProblemasdtiEjView.as_view()), name='problemasdtiejapp'),
    path('matricesejercicios/', login_required(TUMatricesEjView.as_view()), name='matricesejapp'),
    path('menorycofactorejercicios/', login_required(TUMenorCofactorEjView.as_view()), name='menorcofactorejapp'),
    path('eliminaciongaussianaejercicios/', login_required(TUGaussianaEjView.as_view()), name='gaussianaejapp'),
    path('eliminaciongaussjordanejercicios/', login_required(TUGaussJordanEjView.as_view()), name='gaussjordanejapp'),
    path('vectoresejercicios/', login_required(CUVectoresEjView.as_view()), name='vectoresejapp'),
    path('planocartesianoejercicios/', login_required(CUPlanoEjView.as_view()), name='planoejapp'),
    path('determinantesejercicios/', login_required(CUDeterminantesEjView.as_view()), name='determinantesejapp'),
]