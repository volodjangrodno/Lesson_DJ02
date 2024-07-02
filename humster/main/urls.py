from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('clicker/', views.clicker),
    path('community/', views.community),
    path('contact/', views.contact),
]