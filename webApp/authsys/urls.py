from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginpg, name='login'),
    path('logout/', views.logoutpg, name='logout'),
    path('auth/', views.auth, name='auth'),
    path('check/', views.check, name='check'),
]
