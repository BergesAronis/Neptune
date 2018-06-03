from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from login import forms

# Create your views here.

# def index(request):
#     form = forms.LoginForm()
#     return render(request, 'login/index.html', {'form': form})

def index(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('/admin')
            else:
                return render(request, 'login/index.html', {'form': form})
    else:
        form = forms.LoginForm()
    return render(request, 'login/index.html', {'form': form})
