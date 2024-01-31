from django import forms 

class CreateCard(forms.Form):
    side_a = forms.CharField(label="Spanish")
    side_b = forms.CharField(label="English")