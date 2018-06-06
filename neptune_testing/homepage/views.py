from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'homepage/index.html')
