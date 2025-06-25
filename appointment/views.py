from rest_framework import generics
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentListCreate(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
