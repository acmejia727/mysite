from django import forms
from .models import Codigo

class RegForm(forms.Form):
    codigo = forms.CharField(widget=forms.Textarea)
    nombre = forms.CharField(max_length=100)