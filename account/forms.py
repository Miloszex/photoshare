from django.contrib.auth.models import User
from django import forms
#from .models import ExtendedUser
from django.core import validators
from django.forms import ModelForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_repeat_password(self):

        if self.cleaned_data['password'] != self.cleaned_data['repeat_password']:
            raise validators.ValidationError('Passwords are not the same!')
        #return self.cleaned_data['repeat_password']
        return False


class UserLoginForm(forms.Form):

    username = forms.CharField(min_length=1)
    password = forms.CharField(widget=forms.PasswordInput, min_length=1)