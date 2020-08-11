from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
'''
def contact(request, *args, **kwargs):
    return render(request, 'contactApp/contact.html', {})
'''
def contact(request, *args, **kwargs):
    if request.method =='POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Your message has been sent')
            form.save()
        else:
            messages.error(request, 'Your message has not been sent. Make sure you entered the details correctly.')

    else:
        form = ContactForm()
    context = {
        'form': form
    }

    return render(request, 'contactApp/contact.html', context)