from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
    path('users/', include('users.urls')),
]
