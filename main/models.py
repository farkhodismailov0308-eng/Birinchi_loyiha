from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    matn = models.TextField()
    rasm = models.ImageField(upload_to='maqola_rasmlari/', blank=True, null=True)
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)
    manzil = models.CharField(max_length=255, blank=True, null=True, default="Noma'lum")
    telefon = models.CharField(max_length=20, blank=True, null=True, default="Ko'rsatilmagan")

    def __str__(self):
        return self.sarlavha

class Izoh(models.Model):
    maqola = models.ForeignKey(Maqola, on_delete=models.CASCADE, related_name='izohlar')
    muallif = models.CharField(max_length=100)
    matn = models.TextField()
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.muallif} - {self.maqola.sarlavha}"

class Aloqa(models.Model):
    ism = models.CharField(max_length=100)
    email = models.EmailField()
    xabar = models.TextField()
    yuborilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ism}dan xabar"