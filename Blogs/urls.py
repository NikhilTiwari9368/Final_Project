from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),                     
    path('api', views.blog_list, name='blog-api-list'),     
    path('api/add/', views.blog_add, name='blog-api-add'),  
]
