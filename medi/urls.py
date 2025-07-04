"""
URL configuration for medi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from products.views import team


urlpatterns = [
    path("admin/", admin.site.urls),
    path("" , views.index , name = "index"), 
    path("about/" , views.about , name = "about"), 
    path("contact/", views.contact, name="contact"),
    path('contact_form/', include('Contactus.urls')),
    path("contact_view/", views.contact_view, name="contact_view"),
    path('api/', include('appointment.urls')), 
    path("search/" , views.search , name = "search"), 
    path('doctorsearch/', include('DoctorFind.urls')),
    path('team/', team, name='team'),
    path('products/', include('products.urls')),
    path('blog/', include('Blogs.urls')),    
    path("healthcare_centre/", views.healthcare_centre , name="healthcare_centre"),
    path("LoginPage/", views.LoginPage, name="LoginPage"),
    path("LogoutPage/", views.LogoutPage, name="LogoutPage"),
    path("information/", views.information, name="information"),
    path('disease_info/', views.disease_info, name='disease_info'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)