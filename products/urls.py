from django.contrib import admin
from django.urls import path
from . import views
# from django.conf.urls import handler404

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('career/', views.career, name="career"),
    path('contact/', views.contact, name="contact"),
    path('chairman/', views.chairman_view, name='chairman'),
    path('md/', views.md_view, name='md'),
    # path('error_page/',views.error_page,name="error_page"),
    
]
# Correctly set the handler404
# handler404 = 'products.views.error_page'
