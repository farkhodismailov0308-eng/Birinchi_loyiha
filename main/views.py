from django.shortcuts import render
from .models import Maqola

def asosiy_sahifa(request):
    maqolalar = Maqola.objects.all() # Bazadagi hamma maqolalarni oladi
    return render(request, 'index.html', {'maqolalar': maqolalar})