from django import forms
from .models import Ruyxat

class RuyxatForm(forms.ModelForm):
    class Meta:
        model = Ruyxat
        fields = ['first_name', 'last_name', 'tell']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingizni kiriting'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiyangizni kiriting'}),
            'tell': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+998 XX XXX XX XX',
                'type': 'tel',
                'pattern': r'^\+998\s?\d{2}\s?\d{3}\s?\d{2}\s?\d{2}$',
                'required': True
            }),
        }
