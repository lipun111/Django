from django import forms


class Empform(forms.Form):
    name = forms.CharField()
    salary = forms.IntegerField()
    bot = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean(self):
        total_cleaned_data = super().clean()
        inputbot = total_cleaned_data['bot']
        if len(inputbot) > 0:
            raise forms.ValidationError("Welcome BOT")
