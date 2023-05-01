from django.shortcuts import render



def profile(request):
    path = 'settings_profile/profile.html'
    return render(request, path)