from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    matn = models.TextField()
    rasm = models.ImageField(upload_to='maqola_rasmlari/', blank=True, null=True)
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)
    
    # Yangi qo'shilgan maydonlar:
    manzil = models.CharField(max_length=255, blank=True, null=True, default="Noma'lum")
    telefon = models.CharField(max_length=20, blank=True, null=True, default="Ko'rsatilmagan")

    def __str__(self):
        return self.sarlavha