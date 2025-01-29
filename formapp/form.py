
from .models import Ruyxat
from django import forms
#modelform clasi xususiyatlaridan foydalanib forma yaratamiz
class RuyxatForm(forms.ModelForm):
    class Meta:
        #forma shu modelga asoslanib yaratiladi
        model = Ruyxat
        #shu ustunlar olinadi
        fields = ['first_name', 'last_name']
        #widgets orqali html sozlanadi va htmlda kod yozishni kamaytirishimiz mumkin
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }