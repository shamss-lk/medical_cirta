"""medicalcirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import  views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('login/', views.Login),
    path('login_doc/', views.LoginDoc),
    path('signup/', views.Signup),
    path('user/', views.PatientHome),
    path('doctor/', views.DoctorHome),
    path('waitinglist/', views.WaitingList),
    path('doc-message/', views.DocMessage),
    path('logout/', views.Logout),
    path('traitement/', views.Traitement),
    path('remission/', views.Remission),
    path('symptoms/', views.Symp),
    path('historique/', views.Historique),

    path('doc/patients/', views.DocPatient),
    path('doc/patient/<int:id>/', views.PatientDetail),
    path('doc/patient-state/<int:id>/', views.PatientState),
    path('doc/historique-patient/<int:id>/', views.HitoricPatient),
    path('doc/traitement-patient/<int:id>/', views.TraitementPatient),
    path('doc/remission-patient/<int:id>/', views.ResmissionPatient),
    path('doc/symp-patient/<int:id>/', views.SympPatient),
    path('doc/patient/<int:id>/message/', views.DocMessagePatient),
    path('msg_patient/', views.PatientMessageDoc),
    path('delete-noti/', views.DeleteNoti),
    



    path('post-state/', views.PostState),
    path('post-operation/', views.PostOperation),
]
