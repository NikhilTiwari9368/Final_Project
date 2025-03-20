from django.contrib import admin
from appointment.models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('department', 'doctor', 'name', 'email', 'mobile_number', 'appointment_date', 'appointment_time')

admin.site.register(Appointment, AppointmentAdmin)  # Fixed class name capitalization