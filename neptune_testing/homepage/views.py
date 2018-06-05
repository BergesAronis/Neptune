from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from account_handling import forms

def index(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'homepage/index.html', {'form': form})
    else:
        form = forms.LoginForm()
    return render(request, 'homepage/index.html')
