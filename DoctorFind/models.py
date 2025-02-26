from django.db import models

class Doctor(models.Model):
    SPECIALTIES = [
       # Ayurveda Specialties
    ('Ayurveda - General', 'Ayurveda - General'),
    ('Panchakarma Therapy', 'Panchakarma Therapy'),
    ('Marma Therapy', 'Marma Therapy'),
    ('Kshar Sutra Therapy', 'Kshar Sutra Therapy'),
    ('Leech Therapy', 'Leech Therapy'),
    ('Herbal Medicine', 'Herbal Medicine'),
    ('Naturopathy', 'Naturopathy'),
    ('Homeopathy', 'Homeopathy'),

    # Male-Specific Specialties
    ('Andrology (Men’s Health)', 'Andrology (Men’s Health)'),
    ('Ayurvedic Urology', 'Ayurvedic Urology'),

    # Female-Specific Specialties
    ('Gynecology & Obstetrics', 'Gynecology & Obstetrics'),
    ('PCOS & Hormonal Disorders', 'PCOS & Hormonal Disorders'),
    ('Pregnancy & Postpartum Care', 'Pregnancy & Postpartum Care'),

    # Modern Medical Specialties
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

    # Alternative Medicine Specialties
    ('Chiropractic Medicine', 'Chiropractic Medicine'),
    ('Physiotherapy', 'Physiotherapy'),
    ('Acupuncture', 'Acupuncture'),
    ('Unani Medicine', 'Unani Medicine'),
    ('Siddha Medicine', 'Siddha Medicine'), 
    ('Yoga Therapy', 'Yoga Therapy'),
    ]

    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=50, choices=SPECIALTIES)
    city = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
