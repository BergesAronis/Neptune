from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from account_handling import forms


def index(request):
    form = forms.RegistrationForm()
    return render(request, 'homepage/index.html', {'form': form,})
