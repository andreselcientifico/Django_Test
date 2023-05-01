from django.urls import path, include
from . import views

app_name = 'settings_profile'

urlpatterns = [
    path("profile/", views.profile, name="profile")
]
