from django import forms
from .models import Aloqa

class AloqaForm(forms.ModelForm):
    class Meta:
        model = Aloqa
        fields = ['ism', 'email', 'xabar']

from .models import Aloqa, Izoh # Izoh qo'shildi

class IzohForm(forms.ModelForm):
    class Meta:
        model = Izoh
        fields = ['muallif', 'matn']