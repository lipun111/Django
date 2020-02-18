from django import forms
from django.core import validators


class Empform(forms.Form):
    name = forms.CharField()
    salary = forms.IntegerField()
    opinion = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)])

    def clean(self):
        print("Total  form Validation")
        total_cleaned_data = super().clean()
        inputname = total_cleaned_data['name']
        if len(inputname) < 10:
            raise forms.ValidationError("Name must be min 10 chars")
        inputsal = total_cleaned_data['salary']
        if inputsal==0:
            raise forms.ValidationError("sal must be > 0")