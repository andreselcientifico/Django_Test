from django.shortcuts import render,reverse, get_object_or_404
from django.contrib import admin
from django.http import HttpResponse
from .models import Question

def home(request):
    register_url = reverse('users:register')
    Acceso_url = reverse('users:login')
    index_url = reverse('home:index')
    button_link = {
        'register_url': register_url, 
        'Acceso_url':Acceso_url,
        'index_url': index_url,
    }
    path  = 'home/home.html'
    return render(request,path,button_link)

def index(request):
    lastest_question_list = Question.objects.all()
    path = 'home/index.html'
    dic = {
        'lastest_question_list': lastest_question_list,
    }
    return render(request, path, dic)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    path = 'home/detail.html'
    dic = {
        'question':question
    }
    return render(request,path,dic)

def results(request, question_id):
    return HttpResponse(f"Estas Viendo los resultados de la pregunta numero {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas Votando a la pregunta numero {question_id}")