from django import forms
from django.core import validators


def begin_with_S(value):
    if value[0]!='L':
        raise forms.ValidationError("Name Must start with L")
    return


class Empform(forms.Form):
    name = forms.CharField(validators=[begin_with_S])
    salary = forms.IntegerField()
    opinion = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)])
