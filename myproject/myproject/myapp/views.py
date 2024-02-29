from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .models import *

from .forms import contactforms


def index(request):
     images = home.objects.all()
     data = {
         'home':images
     }

     return render(request, 'index.html',data)

def about(request):
       return render(request, 'about.html')

def store(request):

    products = product.objects.all()
    data = {
        'product':products
    }
    return render(request, 'store.html', data)

def contactcreate(request):
    if request.method == 'POST':
        form = contactforms(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = contactforms()
    return render(request, 'contact.html', {'form': form})

