from django.db import models


class Appointment(models.Model):
    
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.department} with {self.doctor} on {self.appointment_date} at {self.appointment_time}"

# Create your models here....