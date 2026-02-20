#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Salom! Bu mening birinchi Django sahifam.")

#(2).config/urls.py faylini oching va uni quyidagicha tahrirlang:
from django.contrib import admin
from django.urls import path
from main.views import index  # Viewni chaqiramiz

urlpatterns = [
    path('admin/', admin.site.path),
    path('', index),  # Asosiy sahifaga ulaymiz
]