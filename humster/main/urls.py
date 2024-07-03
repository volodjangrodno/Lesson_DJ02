from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('clicker/', views.clicker, name='clicker'),
    path('community/', views.community, name='community'),
    path('contact/', views.contact, name='contact'),
]