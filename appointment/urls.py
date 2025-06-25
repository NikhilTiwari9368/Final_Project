from django.urls import path
from .views import AppointmentListCreate

urlpatterns = [
    path('appointments/', AppointmentListCreate.as_view(), name='appointment-api'),
]