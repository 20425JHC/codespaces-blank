from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('films/', views.films, name='films'),
    path('tv_shows/', views.tv_shows, name='tv_shows'),
    path('sign_up/', views.sign_up, name='sign_up'),
]