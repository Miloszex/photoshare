from django.contrib.auth.models import User
from django import forms
from .models import Profile
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


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar']

    def clean_avatar(self):

        avatar = self.cleaned_data.get('avatar', False)
        if avatar:
            if avatar.__size > 1024*1024:
                raise validators.ValidationError('Avatar is Too Large! (>1mb)')
            return avatar




class UserLoginForm(forms.Form):

    username = forms.CharField(min_length=1)
    password = forms.CharField(widget=forms.PasswordInput, min_length=1)