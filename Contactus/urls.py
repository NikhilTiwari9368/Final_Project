from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.contact_list, name='contact-api-list'),
    path('api/add/', views.contact_create, name='contact-api-add'),
]

