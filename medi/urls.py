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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("" , views.index , name = "index"), 
    path("about/" , views.about , name = "about"), 
    path("contact/" , views.contact , name ="contact" ), 
    path("contact_view/", views.contact_view, name="contact_view"),
    path("saveform/" , views.saveform , name = "saveform"), 
    path("search/" , views.search , name = "search"), 
    path("doctorsearch/" , views.doctorsearch , name = "doctorsearch"), 
    path("team/" , views.team , name = "team"), 
    path("blog/",views.blog , name = "blog"),
    path("healthcare_centre/", views.healthcare_centre , name="healthcare_centre"),
    path("LoginPage/", views.LoginPage, name="LoginPage"),
    path("LogoutPage/", views.LogoutPage, name="LogoutPage"),
    path("information/", views.information, name="information"),
    path('disease_info/', views.disease_info, name='disease_info'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)