from django.contrib import admin
from .models import Maqola, Aloqa, Izoh

# 1. Maqolalar uchun mukammal admin sozlamalari
@admin.register(Maqola)
class MaqolaAdmin(admin.ModelAdmin):
    # Jadvalda ko'rinadigan ustunlar
    list_display = ('sarlavha', 'yaratilgan_sana', 'manzil', 'telefon')
    # O'ng tomondagi filtrlar paneli
    list_filter = ('yaratilgan_sana', 'manzil')
    # Sarlavha va matn bo'yicha qidiruv
    search_fields = ('sarlavha', 'matn')
    # Sana bo'yicha yuqorida navigatsiya (yil, oy, kun)
    date_hierarchy = 'yaratilgan_sana'

# 2. Aloqa xabarlari (Contact messages) uchun sozlamalar
@admin.register(Aloqa)
class AloqaAdmin(admin.ModelAdmin):
    list_display = ('ism', 'email', 'yuborilgan_vaqt')
    search_fields = ('ism', 'email', 'xabar')
    list_filter = ('yuborilgan_vaqt',)
    # Vaqtni tahrirlab bo'lmaydigan (faqat ko'rinadigan) qilish
    readonly_fields = ('yuborilgan_vaqt',)

# 3. Izohlar (Comments) uchun sozlamalar
@admin.register(Izoh)
class IzohAdmin(admin.ModelAdmin):
    list_display = ('muallif', 'maqola', 'yaratilgan_sana')
    list_filter = ('yaratilgan_sana', 'maqola')
    search_fields = ('muallif', 'matn')