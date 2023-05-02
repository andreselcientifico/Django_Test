from django.shortcuts import render,reverse



def profile(request):
    path = 'settings_profile/profile.html'
    return render(request, path)