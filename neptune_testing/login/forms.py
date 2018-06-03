from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, help_text='Enter username.')
    password = forms.CharField(max_length=30, required=True, help_text='Enter password.', widget=forms.PasswordInput)
