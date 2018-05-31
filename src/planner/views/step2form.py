from django import forms

class Step2Form(forms.Form):
    elec1 = forms.CharField(widget=forms.NumberInput,label='Elective 1 ID',min_length=5,max_length=5)
    elec2 = forms.CharField(widget=forms.NumberInput,label='Elective 2 ID',min_length=5,max_length=5)
    elec3 = forms.CharField(widget=forms.NumberInput,label='Elective 3 ID',min_length=5,max_length=5,required=False)
    elec4 = forms.CharField(widget=forms.NumberInput,label='Elective 4 ID',min_length=5,max_length=5,required=False)
    elec5 = forms.CharField(widget=forms.NumberInput,label='Elective 5 ID',min_length=5,max_length=5,required=False)
    elec6 = forms.CharField(widget=forms.NumberInput,label='Elective 6 ID',min_length=5,max_length=5,required=False)
    elec7 = forms.CharField(widget=forms.NumberInput,label='Elective 7 ID',min_length=5,max_length=5,required=False)
