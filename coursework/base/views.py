from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def welcome(request):
    return render(request, 'base/welcome.html')

def about(request):
	return render(request, 'base/about.html')

def projects(request):
	return render(request, 'base/projects.html')

def contact(request):
	return render(request, 'base/contact.html')