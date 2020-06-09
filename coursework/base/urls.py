from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.home),
    path('', views.welcome),
    path('about/', views.about),
    path('contact/', views.contact),
    path('projects/', views.projects),
    
]