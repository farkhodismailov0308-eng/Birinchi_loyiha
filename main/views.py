from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Maqola, Izoh, Aloqa

# 1. Barcha maqolalar ro'yxati
def asosiy_sahifa(request):
    maqolalar = Maqola.objects.all().order_by('-yaratilgan_sana')
    return render(request, 'index.html', {'maqolalar': maqolalar})

# 2. Maqola detali, Izohlar va Ariza qoldirish mantiqi
def batafsil_view(request, pk):
    maqola = get_object_or_404(Maqola, pk=pk)
    # Maqolaga tegishli izohlarni olish
    izohlar = maqola.izohlar.all().order_by('-yaratilgan_sana')
    
    if request.method == "POST":
        # HTML formadagi tugma nomiga (name) qarab ajratamiz
        
        # A) AGAR ARIZA (ALOQA) YUBORILSA
        if 'ariza_tugmasi' in request.POST:
            ism = request.POST.get('ism', '').strip()
            email = request.POST.get('email', '').strip()
            xabar = request.POST.get('xabar', '').strip()
            
            if ism and email and xabar:
                Aloqa.objects.create(ism=ism, email=email, xabar=xabar)
                messages.success(request, "Arizangiz muvaffaqiyatli yuborildi!")
                return redirect('detail', pk=pk)
            else:
                messages.error(request, "Iltimos, ariza maydonlarini to'ldiring!")

        # B) AGAR IZOH YUBORILSA
        elif 'izoh_tugmasi' in request.POST:
            muallif_ismi = request.POST.get('ism', '').strip()
            izoh_matni = request.POST.get('izoh_matni', '').strip() # HTMLda name="izoh_matni" bo'lishi kerak
            
            if muallif_ismi and izoh_matni:
                Izoh.objects.create(
                    maqola=maqola,
                    muallif=muallif_ismi,
                    matn=izoh_matni
                )
                messages.success(request, "Izohingiz muvaffaqiyatli qo'shildi!")
                return redirect('detail', pk=pk)
            else:
                messages.error(request, "Iltimos, izoh maydonini to'ldiring!")

    context = {
        'maqola': maqola,
        'izohlar': izohlar,
    }
    return render(request, 'detail.html', context)