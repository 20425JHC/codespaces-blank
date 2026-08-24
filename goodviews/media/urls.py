from django.urls import path
from . import views

#url patterns for all pages
urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('films/', views.films, name='films'),
    path('tv_shows/', views.tv_shows, name='tv_shows'),
]