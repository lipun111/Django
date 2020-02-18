from django import forms


class Empform(forms.Form):
    Name = forms.CharField()
    Sal = forms.IntegerField()