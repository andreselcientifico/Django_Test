from django.shortcuts import render,reverse
from django.http import HttpResponse


def home(request):
    register_url = reverse('users:register')
    Acceso_url = reverse('users:login')
    button_link = {
        'register_url': register_url, 
        'Acceso_url':Acceso_url
    }
    path  = 'home/home.html'
    return render(request,path,button_link)