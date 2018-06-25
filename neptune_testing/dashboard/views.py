from django.shortcuts import render, redirect
from .models import Navigation


def index(request):
    navigation_apps = Navigation.objects.values()
    return render(request, 'dashboard/dashboard.html',  {'navigation_apps': navigation_apps})
