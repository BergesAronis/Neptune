from django.shortcuts import render, redirect

def index(request):
    return render(request, 'dashboard/dashboard.html')

def to_do_list(request):
    return render(request, 'to_do_list/to_do_list.html')
