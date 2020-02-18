from django import forms
from webapp.models import Filter


class Filterform(forms.ModelForm):
    class Meta:
        model = Filter
        fields = '__all__'
        
