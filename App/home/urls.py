from django.urls import path, include
from django.contrib import admin
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('users/', include('users.urls'), name='users'),
]
