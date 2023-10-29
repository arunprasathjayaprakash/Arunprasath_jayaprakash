from django import forms
class FormFields(forms.Form):
    name = forms.CharField(label="name", max_length=200)
    email = forms.CharField(label='mail_id')