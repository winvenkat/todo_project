from django import forms
from django.forms import ModelForm

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
	targetdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
	notes = forms.CharField()

	class Meta:
		model = Task
		fields = ['title','targetdate','notes']
		widgets = {
            'targetdate': DateInput(),
        }