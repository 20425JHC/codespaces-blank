from django.shortcuts import render
from .models import films as FilmsModel, tv_shows as TVShowsModel

#home page
def home(request):
    return render(request, 'home.html')

#films page
def films(request):
    all_films = FilmsModel.objects.all()
    context = {
        'films': all_films,
    }
    return render(request, 'films.html', context)

#tv shows page
def tv_shows(request):
    all_tv_shows = TVShowsModel.objects.all()
    context = {
        'tv_shows': all_tv_shows,
    }
    return render(request, 'tv_shows.html', context)

#sign up page:
def sign_up(request):
    return render(request, 'sign_up.html')