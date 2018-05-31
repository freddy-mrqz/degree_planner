from django import forms


SUBJECTS = (('CS',"Computer Science"),('IS',"Information Systems"))
SEASON = (('1',"Fall"),('2',"Winter"),('3',"Spring"))
IS_CON = (
        ('Standard','Standard'),
        ('Systems Analysis','Systems Analysis'),
        ('Business Intelligence','Business Intelligence'),
        ('Database Administration','Database Administration'),
        ('Enterprise Infrastructure','Enterprise Infrastructure')
        )
CS_CON = (
        ('Software and Systems Development','Software and Systems Development'),
        ('Theory','Theory'),
        ('Data Science','Data Science'),
        ('Artificial Intelligence','Artificial Intelligence'),
        ('Game and Real-Time Systems','Game and Real-Time Systems'),
        ('Human-Computer Interaction','Human-Computer Interaction')
        )
CLASSES_PER = (('1','One per term'),('2','Two per term'),('3','Three per term'))

class PathForm(forms.Form):
    subject = forms.ChoiceField(widget=forms.RadioSelect,choices=SUBJECTS)
    cs_con = forms.ChoiceField(widget=forms.Select,choices=CS_CON)
    is_con = forms.ChoiceField(widget=forms.Select,choices=IS_CON)
    num = forms.ChoiceField(widget=forms.Select,choices=CLASSES_PER)
    start = forms.ChoiceField(widget=forms.RadioSelect,choices=SEASON)
