from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.

def check(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login/')
    else:
        return redirect('/worker/')

def loginpg(request):
    return render(request, 'registration/login.html')


def logoutpg(request):
    logout(request)    
    return render(request, 'registration/logout.html')



def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/worker/')
    else:
        return render(request, 'registration/login_error.html')
