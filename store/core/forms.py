from django import forms
from . import models

class InvoiceForm(forms.ModelForm):
    class Meta:
        models=models.Invoice
        fields=['address']