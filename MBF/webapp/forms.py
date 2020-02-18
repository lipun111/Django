from django import forms
from webapp.models import Emp
from django.core import validators


class Empform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        total_cleaned_data = super().clean()
        inputpswd = total_cleaned_data['password']
        inputrpswd = total_cleaned_data['rpassword']

        if inputpswd != inputrpswd:
            raise forms.ValidationError("Password Not Match")

    class Meta:
        model = Emp
        fields = ('name', 'eid', 'salary',)
