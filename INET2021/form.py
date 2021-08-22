from django.forms import ModelForm
from django import forms

class CalculateCap(forms.Form):
    option = forms.BooleanField(required=False)
