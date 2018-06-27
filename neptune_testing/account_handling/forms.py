from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import User, Client

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Client
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, help_text='Enter username.')
    password = forms.CharField(max_length=30, required=True, help_text='Enter password.', widget=forms.PasswordInput)
