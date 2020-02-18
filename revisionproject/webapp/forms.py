from django import forms
from webapp.models import Revision

class RevisionForm(forms.ModelForm):
    class Meta:
        model= Revision
        fields ='__all__'
        
