from django import forms
from django.forms import ModelForm
from django.core.validators import MinValueValidator, MaxValueValidator

from barbers.models import Barber

class BarberForm(ModelForm):
    class Meta:
        model = Barber
        fields = ["name", "photo", "experience", "birthdate", "position", "gender", "phone"]
        widgets = {
            'birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "photo": forms.ClearableFileInput(attrs={'class': 'form-control'}),
            "position": forms.Select(attrs={'class': 'form-select'}),
            "gender": forms.Select(attrs={'class': 'form-select'}),
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter barber name'}),
            "experience": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter years of experience'}),
            "phone": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number', "type": "tel"}),
        }
    
# class BarberSearchForm(forms.Form):
#     text = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search barbers...'}))
