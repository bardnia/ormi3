# main > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inxex'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact, name='contact'),
]