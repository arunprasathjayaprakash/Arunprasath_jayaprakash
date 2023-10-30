from django import forms
class FormFields(forms.Form):
    name = forms.CharField(label='Name',max_length=200)
    email = forms.CharField(required=False)