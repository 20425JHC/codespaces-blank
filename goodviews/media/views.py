from django.shortcuts import render
from .models import films as FilmsModel, tv_shows as TVShowsModel

#home page
def home(request):
    return render(request, 'home.html')

#Good views
def goodviews(request):
    return render(request, 'goodviews.html')

#films page
def films(request):
    selected_genre = request.GET.get('genre')
    selected_age_rating = request.GET.get('age_rating')

    if selected_genre:
        #filter films using foreign key in genre
        all_films = FilmsModel.objects.filter(genre__genre__iexact=selected_genre)
    if selected_age_rating:
        all_films = FilmsModel.objects.filter(age_rating__age_rating__iexact=selected_age_rating)
    else:
        all_films = FilmsModel.objects.all()

    context = {
        'films': all_films,
        'selected_genre': selected_genre,
        'selected_age_rating': selected_age_rating, 
    }
    return render(request, 'films.html', context)

#tv shows page
def tv_shows(request):
    selected_genre = request.GET.get('genre')
    
    if selected_genre:
            #filter shows using foreign key in genre
        all_tv_shows = TVShowsModel.objects.filter(genre__genre__iexact=selected_genre)
    else:
        all_tv_shows = TVShowsModel.objects.all()
    
    context = {
        'tv_shows': all_tv_shows,
        'selected_genre': selected_genre, 
        }
    return render(request, 'tv_shows.html', context)

#sign up page:
def sign_up(request):
    return render(request, 'sign_up.html')