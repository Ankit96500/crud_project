from django import forms
from enroll.models import studentdb

class studentform(forms.ModelForm):
    class Meta:
        model=studentdb
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=False,attrs={'class':'form-control'}),
        }