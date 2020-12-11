from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
def main_scr(request):
    return render(request, 'worker_scr_main.html')
