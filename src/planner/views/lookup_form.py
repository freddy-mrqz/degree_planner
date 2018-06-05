from django import forms

class LookupForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput,label='name')
