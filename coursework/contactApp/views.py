from django.shortcuts import render

# Create your views here.

def contact(request, *args, **kwargs):
	return render(request, 'contactApp/contact.html', {})
