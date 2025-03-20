from django.db import models


class Appointment(models.Model):
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)  # Added mobile number field
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"{self.name} ({self.mobile_number}) - {self.department} with {self.doctor} on {self.appointment_date} at {self.appointment_time}"
