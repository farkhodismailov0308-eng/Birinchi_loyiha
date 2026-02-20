from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    matn = models.TextField()
class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    matn = models.TextField()
    # Yangi maydon:
    rasm = models.ImageField(upload_to='maqola_rasmlari/', blank=True, null=True)
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sarlavha