from django import forms

class studentform(forms.Form):
    s_name=forms.CharField(max_length=50)
    s_class=forms.CharField(max_length=50)
    s_address=forms.CharField(max_length=50)
    s_faculty=forms.CharField(max_length=50)
    s_mail=forms.CharField(max_length=50)
    
class SForm(forms.Form):
    s_name=forms.CharField(max_length=50)