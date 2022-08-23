from django.forms import ModelForm
from django import forms
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'author', 'date', 'description']

class DateForm(forms.Form):
    date = forms.DateField(input_formats=['%d-%m-%Y'])
