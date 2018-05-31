from django.shortcuts import render
import datetime

from registration import forms

# Create your views here.

def index(request):
    form = forms.RegistrationForm()
    return render(request, 'registration/index.html', {'form': form})
