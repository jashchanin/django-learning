
from django.http import HttpResponse
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name="contact"),
    path('polls/', views.index, name='index'),
]