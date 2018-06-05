from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm


def index(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            print('logout')
            logout(request)
            return redirect('/')
        elif 'login' in request.POST:
            username = request.POST.get("username", "")
            raw_password = request.POST.get("password", "")
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'homepage/index.html')
    return render(request, 'homepage/index.html')
