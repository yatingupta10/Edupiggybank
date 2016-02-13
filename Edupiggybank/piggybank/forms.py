from django import forms

from .models import Passbook

class PassbookForm(forms.ModelForm):

    class Meta:
        model = Passbook
        fields = ('name', 'text','created_date','transaction')