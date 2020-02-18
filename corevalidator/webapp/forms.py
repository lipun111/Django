from django import forms
from django.core import validators


class Empform(forms.Form):
    name = forms.CharField()
    salary = forms.IntegerField()
    opinion = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)])
