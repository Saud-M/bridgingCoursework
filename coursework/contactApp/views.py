from django.shortcuts import render

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
            form.save()

    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contactApp/contact.html', context)