from django.urls import path
from . import views

#my code:
#url patterns for all pages: tells programme the directory of how to find the files to display on teh wesbite which are connected to views (makes the file viewable)
urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('films/', views.films, name='films'),
    path('tv_shows/', views.tv_shows, name='tv_shows'),
]