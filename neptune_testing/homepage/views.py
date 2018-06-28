from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from account_handling import forms


def index(request):
    form = forms.RegistrationForm()
    client_form = forms.ClientRegistrationForm()
    staff_form = forms.StaffRegistrationForm()
    agent_form = forms.AgentRegistrationForm()
    context = {
        'form': form,
        'client_form': client_form,
        'staff_form': staff_form,
        'agent_form': agent_form,
    }
    return render(request, 'homepage/index.html', context)
