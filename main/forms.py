from django import forms

from .models import *


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file',)

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('char',)
