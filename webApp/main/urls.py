from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about/', views.about, name='about'),
    path('maps/', views.maps, name='maps'),
    path('workers/', views.workers, name='workers'),
]
