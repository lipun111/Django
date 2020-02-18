from django import forms
from webapp.models import Signup


class Signupform(forms.ModelForm):
    class Meta:
        model = Signup
        fields ='__all__'
