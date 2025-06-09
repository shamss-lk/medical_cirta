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

from .views import llm_page, query_llm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('login/', views.Login),
    path('login_doc/', views.LoginDoc),
    path('signup/', views.Signup),
    path('user/', views.PatientHome , name='user'),
    path('doctor/', views.DoctorHome),
    path('waitinglist/', views.WaitingList),
    path('doc-message/', views.DocMessage),
    path('logout/', views.Logout, name='logout'),
    path('traitement/', views.Traitement, name='traitement'), 
    path('remission/', views.Remission, name='remission'),
    path('symptoms/', views.Symp, name='symp'),
    path('historique/', views.Historique, name='historique'),

    path("llm/", llm_page, name="llm_page"),
    path("api/llm/", query_llm, name="query_llm"),

    path('doc/patients/', views.DocPatient),
    path('doc/patient/<int:id>/', views.PatientDetail),
    path('doc/patient-state/<int:id>/', views.PatientState),
    path('doc/historique-patient/<int:id>/', views.HitoricPatient),
    path('doc/traitement-patient/<int:id>/', views.TraitementPatient),
    path('doc/remission-patient/<int:id>/', views.ResmissionPatient),
    path('doc/symp-patient/<int:id>/', views.SympPatient),
    path('doc/patient/<int:id>/message/', views.DocMessagePatient),
    path('msg_patient/', views.PatientMessageDoc, name='msg_patient'),
    path('delete-noti/', views.DeleteNoti),
    

    path('post-state/', views.PostState),
    path('post-operation/', views.PostOperation),
    path('dashboard/', views.patient_dashboard, name='dashboard'),

#     path('dashboard/', views.patient_dashboard, name='dashboard'),
# path('logout/', views.logout_view, name='logout'),

# path('add/flare/', views.add_flare, name='add_flare'),
# path('add/health-status/', views.add_health_status, name='add_health_status'),
# path('add/cdai/', views.add_cdai, name='add_cdai'),
# path('add/treatment/', views.add_treatment, name='add_treatment'),
# path('add/diet/', views.add_diet, name='add_diet'),
# path('add/exam/', views.add_exam, name='add_exam'),

]
