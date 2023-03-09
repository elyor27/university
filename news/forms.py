from django import forms
from .models import *


class NewsModelForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        exclude = ['created_at']
