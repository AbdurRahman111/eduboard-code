from django import forms
from django.db import models
from django.forms import fields
from .models import FormData

class EduboardForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = '__all__'