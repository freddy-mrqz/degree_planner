from django import forms

class LookupForm(forms.Form):
    fullname = forms.CharField(label='name')
