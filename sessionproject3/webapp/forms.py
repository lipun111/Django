from django import forms


class AddForm(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()

