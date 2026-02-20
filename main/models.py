from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    matn = models.TextField()
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sarlavha