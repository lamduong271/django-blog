from django.urls import path
# Calling views.py in /home
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact, name="contact"),
    path('register/', views.register, name="register"),

]
