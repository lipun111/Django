from django import forms
from django.contrib.auth.models import User
from webapp.models import Employee


class InsertForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields ='__all__'


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username', 'password', 'email', 'first_name', 'last_name']
