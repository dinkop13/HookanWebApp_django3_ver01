from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_scr, name='workersrc_main'),
]
