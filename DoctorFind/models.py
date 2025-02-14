from django.db import models

class Doctor(models.Model):
    SPECIALTIES = [
        ('Ayurveda', 'Ayurveda'),
        ('Herbal Medicine', 'Herbal Medicine'),
        ('Naturopathy', 'Naturopathy'),
        ('Homeopathy', 'Homeopathy'),
        ('Cardiology', 'Cardiology'),
        ('Dermatology', 'Dermatology'),
        ('Neurology', 'Neurology'),
        ('Pediatrics', 'Pediatrics'),
        ('Psychiatry', 'Psychiatry'),
        ('Radiology', 'Radiology'),
        ('Surgery', 'Surgery'),
        ('Orthopedics', 'Orthopedics'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Oncology', 'Oncology'),
    ]

    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=50, choices=SPECIALTIES)
    city = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
