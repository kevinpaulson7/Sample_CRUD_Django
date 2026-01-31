from django import forms
from .models import Bike

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['brand', 'model', 'price', 'mileage', 'is_available']
        