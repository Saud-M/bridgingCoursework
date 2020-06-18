from django.shortcuts import render

# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'base/home.html', {})

def welcome(request, *args, **kwargs):
    return render(request, 'base/welcome.html', {})

def about(request, *args, **kwargs):
	return render(request, 'base/about.html', {})

def projects(request, *args, **kwargs):
	return render(request, 'base/projects.html', {})

def contact(request, *args, **kwargs):
	return render(request, 'base/contact.html', {})