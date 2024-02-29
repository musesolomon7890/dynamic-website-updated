# forms.py
from django import forms
from .models import contact_us




class contactforms(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = ['name', 'email', 'message']


