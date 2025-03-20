from django.contrib import admin


from DoctorFind.models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'speciality', 'city','contact_info' ,'image')

admin.site.register(Doctor, DoctorAdmin) 

# Register your models here.
