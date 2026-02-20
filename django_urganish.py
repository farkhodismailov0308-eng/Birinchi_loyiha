# DJANGO-PYTHON - NOLDAN URGANISH
"""
Created on Sun Feb  8 15:31:41 2026

@author: Farhod Ismoilov

Asistent/Agent AI=SI: https://gemini.google.com/share/continue/251aa5777226
"""

#Noldan boshlayotgan bo'lsangiz, juda soz! Django o'rganishni boshlash uchun kompyuteringizda Python o'rnatilgan bo'lishi kerak.

#Keling, birinchi loyihangizni birgalikda qadam-baqadam quramiz:

#1-qadam: Virtual muhit (Virtual Environment) yaratish
#Dasturlashda loyihalarni bir-biridan ajratib saqlash juda muhim. Bu boshqa kutubxonalar bilan chalkashlikning oldini oladi.

#Terminal (yoki CMD)ni ochib, loyiha uchun papka oching va ichiga kiring:
#Bash 
mkdir my_django_project
cd my_django_project

#Virtual muhitni yarating va ishga tushiring:

#Windows:
python -m venv venv
venv\Scripts\activate
    
#Mac/Linux:
python3 -m venv venv
source venv/bin/activate

#2-qadam: Django-ni o'rnatish
#Virtual muhit faol bo'lgandan keyin (qavs ichida (venv) yozuvi chiqadi), Djangoni yuklaymiz:
pip install django

#3-qadam: Loyiha yaratish
#Endi asosiy loyiha fayllarini generatsiya qilamiz. Loyihani config deb nomlashni tavsiya qilaman (tuzilma tushunarli bo'lishi uchun):
django-admin startproject config .

#(Oxiridagi nuqta . loyihani hozirgi papkaning ichida ochishini bildiradi).

#4-qadam: Serverni ishga tushirish
#Hamma narsa to'g'ri bo'lganini tekshirish uchun serverni yoqing:
   
python manage.py runserver

#Brauzeringizda http://127.0.0.1:8000/ manzili bo'yicha kirib ko'ring. Agar "The install worked successfully" yozuvi va raketani ko'rsangiz — tabriklayman!   

#5-qadam: Ilova (App) yaratish
#Django loyihasi bir nechta kichik "ilova"lardan tashkil topadi (masalan: blog, savdo, login tizimi). Keling, birinchi ilovamizni yaratamiz:
    
python manage.py startapp main

#Endi bu ilovani loyihaga tanitish kerak:

#config/settings.py faylini oching.

#INSTALLED_APPS ro'yxatiga 'main', so'zini qo'shing.

#6-qadam: "Hello World" (Birinchi sahifa)
#(1).main/views.py faylini oching va mana bu kodni yozing:
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

#Natija
#erverni qayta ishga tushiring (agar o'chgan bo'lsa) va sahifani yangilang. Siz ekranda o'zingiz yozgan matnni ko'rasiz.

#Keyingi qadamda nima qilamiz? Sizga Ma'lumotlar bazasi (Models) bilan ishlashni ko'rsatib beraymi yoki tayyor Admin Panelga kirishni o'rganamizmi?