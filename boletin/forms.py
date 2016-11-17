from django import forms
from .models import Codigo

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Codigo
        fields = ['nombre','codigo']


class RegForm(forms.Form):
    codigo = forms.CharField(widget=forms.Textarea)
    nombre = forms.CharField(max_length=100)