from django.urls import path
from . import views

urlpatterns = [
    path('team/', views.team, name='team'),  # ✅ This makes {% url 'team' %} work
    path('api/', views.product_list, name='product-api-list'),
    path('api/add/', views.product_add, name='product-api-add'),
]
