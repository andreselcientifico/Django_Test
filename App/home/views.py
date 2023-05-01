from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, reverse

# Create your views here.
def home(request):
    register_url = reverse('users:register')
    Acceso_url = reverse('users:login')
    button_link = {
        'register_url': register_url, 
        'Acceso_url':Acceso_url
    }
    return render(request,'home/home.html', button_link)