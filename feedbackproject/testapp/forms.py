from django import forms
from django.core import validators


class FeedbackForm(forms.Form):
    name = forms.CharField()
    rollno= forms.IntegerField()
    email = forms.EmailField()
    password= forms.CharField(label='Password', widget= forms.PasswordInput)
    rpassword= forms.CharField(label='Re-Enter Password', widget= forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    bot = forms.CharField(required=False, widget= forms.HiddenInput)

    def clean(self):
        total_cleaned_data = super().clean()
        inputname= total_cleaned_data['name']
        if len(inputname)<5:
            raise forms.ValidationError("Name must be grater than five charecter")
        inputrollno = total_cleaned_data['rollno']
        if len(str(inputrollno))<4:
            raise forms.ValidationError("RollNo must be grater than four charecter")

        inputpwd = total_cleaned_data['password']
        inputrpwd = total_cleaned_data['rpassword']
        if inputpwd != inputrpwd :
            raise forms.ValidationError("Password Not Match")

        inputbot = total_cleaned_data['bot']
        if len(inputbot)>0:
            raise forms.ValidationError("Welcome BOT..")
