from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.core import validators
from django.forms import ModelForm
import os

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


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar']


class UserLoginForm(forms.Form):

    username = forms.CharField(min_length=1)
    password = forms.CharField(widget=forms.PasswordInput, min_length=1)