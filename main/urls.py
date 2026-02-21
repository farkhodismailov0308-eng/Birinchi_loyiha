from django.urls import path
from .views import asosiy_sahifa, batafsil_view

urlpatterns = [
    path('', asosiy_sahifa, name='home'),
    path('maqola/<int:pk>/', batafsil_view, name='detail'),
]