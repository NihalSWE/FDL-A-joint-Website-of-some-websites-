from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('career/', views.career, name="career"),
    path('contact/', views.contact, name="contact"),
    path('chairman/', views.chairman_view, name='chairman'),
    path('md/', views.md_view, name='md'),
    
]