from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'landing/landing_index.html')


def about(request):
    return render(request, 'landing/landing_about.html')


def maps(request):
    return render(request, 'landing/landing_maps.html')


def workers(request):
    return render(request, 'landing/landing_workers.html')
