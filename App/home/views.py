from django.shortcuts import render,reverse
from django.contrib import admin
from django.http import HttpResponse
from .models import Question

def home(request):
    register_url = reverse('users:register')
    Acceso_url = reverse('users:login')
    button_link = {
        'register_url': register_url, 
        'Acceso_url':Acceso_url
    }
    path  = 'home/home.html'
    return render(request,path,button_link)

def index(request):
    latest_question_list = Question.objects.all()
    path = 'home/index.html'
    dic = {
        'latest_question_list': latest_question_list,
    }
    return render(request, path, dic)