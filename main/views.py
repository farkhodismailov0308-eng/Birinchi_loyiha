from django.shortcuts import render
from .models import Maqola

def asosiy_sahifa(request):
    maqolalar = Maqola.objects.all() # Bazadagi hamma maqolalarni oladi
    return render(request, 'index.html', {'maqolalar': maqolalar})

from django.shortcuts import render, get_object_or_404
from .models import Maqola

def asosiy_sahifa(request):
    maqolalar = Maqola.objects.all()
    return render(request, 'index.html', {'maqolalar': maqolalar})

def batafsil_view(request, pk):
    # Bu funksiya maqolani ID (pk) orqali topadi, topilmasa 404 xatosini beradi
    maqola = get_object_or_404(Maqola, pk=pk)
    return render(request, 'detail.html', {'maqola': maqola})

from .models import Maqola

def batafsil_view(request, pk):
    maqola = Maqola.objects.get(pk=pk) # ID orqali maqolani topamiz
    return render(request, 'detail.html', {'maqola': maqola})