from django import forms
from django.forms import ModelForm
from .models import Music

class MusicForm(forms.ModelForm):
    video = forms.FileField(label='Video file')
    class Meta:
    	model = Music
    	fields = {'video'}