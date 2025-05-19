from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['word', 'translation', 'image']

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()
