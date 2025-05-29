from django.urls import path
from . import views

urlpatterns = [
    path('video-requests/', views.view_requests, name='view_requests'),
    path('accept-call/<int:request_id>/', views.accept_call, name='accept_call'),
    path('request-call/', views.request_call_view, name='request_call'),   # shows doctor list
    path('request_call/', views.initiate_call, name='initiate_call'),      # handles form

    path('view-requests/', views.view_requests, name='view_requests'),  
]
