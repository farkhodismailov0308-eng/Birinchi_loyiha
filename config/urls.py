from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import asosiy_sahifa, batafsil_view # Funksiya nomlarini tekshiring

urlpatterns = [
    path('admin/', admin.site.urls), # Admin panel qaytishi kerak
    path('', asosiy_sahifa, name='home'), # Asosiy sahifa
    path('maqola/<int:pk>/', batafsil_view, name='detail'), # Batafsil sahifa
]

# Mana bu qism urlpatterns ro'yxatidan TASHQARIDA, oxirida bo'lishi kerak:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)