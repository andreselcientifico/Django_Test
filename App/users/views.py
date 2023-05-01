from django.shortcuts import render, reverse
from django.http import HttpResponse



# Create your views here.
def index(request):
    profile_url = reverse('settings_profile:profile')
    button_link ={
        'profile_url': profile_url
    }
    path = 'users/login.html'
    return render(request, path, button_link)


def register(request):
    return render(request,'users/register.html')

def About(request):
    return render(request, 'users/About.html')