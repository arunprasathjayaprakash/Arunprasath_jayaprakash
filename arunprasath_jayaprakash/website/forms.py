import datetime

from django import forms
from django.db import models

class FormFields(forms.Form):
    name = forms.CharField(label='Name',max_length=200)
    email = forms.EmailField(required=True)
    notes = forms.CharField(required=False,max_length=5000)

class UpdateForm(forms.Form):
    id = forms.IntegerField(disabled=True)
    name = forms.CharField(label='Name', max_length=200)
    email = forms.EmailField(required=True)
    notes = forms.CharField(required=False, max_length=5000)

class DeleteForm(forms.Form):
    id = forms.IntegerField(disabled=True)
    name = forms.CharField(disabled=True)
    email = forms.EmailField(disabled=True)
    notes = forms.CharField(disabled=True)

class Contacts(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    notes = models.CharField(max_length=500)
    created_time = models.TimeField(auto_now_add=True)

# class Tables(table.Tables)