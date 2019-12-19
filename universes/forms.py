from django import forms

from .models import Universe

class UniverseCreateForm(forms.ModelForm):
    class Meta:
        model = Universe
        fields = '__all__'