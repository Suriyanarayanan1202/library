from django import forms
from .models import *

class book_forms(forms.ModelForm):
    class Meta:
        model = book_models
        fields = '__all__'

class transaction_forms(forms.ModelForm):
    class Meta:
        model = transaction_model
        fields = ['book','customer']
