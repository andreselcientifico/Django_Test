from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    #ex: /users/
    path("login/", views.index, name="login"),
    #ex: /users/register
    path("register/", views.register, name="register"),
    #ex: /users/About
    path("About/", views.About, name="About"),

    path('settings_profile/', include('settings_profile.urls')),
]