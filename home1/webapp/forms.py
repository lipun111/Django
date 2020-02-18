from django import forms
from webapp.models import Gpl


class Gplform(forms.ModelForm):
    class Meta:
        model = Gpl
        fields = '__all__'