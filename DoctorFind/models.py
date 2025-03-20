from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)  # Free text specialty
    city = models.CharField(max_length=100)
    contact_info = models.TextField()
    image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)  # Image field

    def __str__(self):
        return self.name