from django import forms

from .models import Universe, Place

class UniverseCreateForm(forms.ModelForm):
    class Meta:
        model = Universe
        fields = '__all__'

class PlaceCreateForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'