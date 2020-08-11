from django.shortcuts import render

# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'base/home.html', {})

def welcome(request, *args, **kwargs):
    return render(request, 'base/welcome.html', {})
