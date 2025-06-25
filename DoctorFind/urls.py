# DoctorFind/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('doctorsearch/', views.doctorsearch, name='doctorsearch'),  # existing search view
    path('api/doctors/', views.doctor_list, name='api-doctor-list'),
    path('api/doctors/add/', views.add_doctor, name='api-add-doctor'),
]
