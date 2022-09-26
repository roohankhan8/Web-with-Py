import imp
from unicodedata import name
from django.shortcuts import render, HttpResponse
# from datetime import datetime
from home.models import Contact
# from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def store(request):
    return render(request, 'store.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    if request.method == 'POST':
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            number = request.POST.get('number'),
            contact = Contact(name=name, email=email, number=number)
            contact.save()
            # messages.success(request, 'Profile details updated!')
    return render(request, 'contact.html')
