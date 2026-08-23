from django.shortcuts import render
from .models import films as FilmsModel, tv_shows as TVShowsModel, genre as GenreModel, age_rating as AgeRatingModel

#home page
def home(request):
    selected_year_of_release = request.GET.get('year_of_release')

    all_films = FilmsModel.objects.filter(year_of_release__gte='2020').values()
    all_tv_shows = TVShowsModel.objects.filter(year_of_release__gte='2020').values()
    
    context = {
        'films': all_films,
        'tv_shows' : all_tv_shows,
        'selected_year_of_release' : selected_year_of_release 
        }
    return render(request, 'home.html', context)

#Good views
def contact_us(request):
    return render(request, 'contact_us.html')

#films page
def films(request):
    selected_genre_id = request.GET.get('genre')
    selected_age_rating_id = request.GET.get('age_rating')

    all_films = FilmsModel.objects.all()

    if selected_genre_id:
        #filter films using foreign key in genre
        all_films = FilmsModel.objects.filter(genre_id=selected_genre_id)
    if selected_age_rating_id:
        all_films = FilmsModel.objects.filter(age_rating_id=selected_age_rating_id)

    context = {
        'films': all_films,
        'genres' : GenreModel.objects.all(),
        'age_ratings' : AgeRatingModel.objects.all(),
        'selected_genre': selected_genre_id,
        'selected_age_rating': selected_age_rating_id, 
    }
    return render(request, 'films.html', context)

#tv shows page
def tv_shows(request):
    selected_genre_id = request.GET.get('genre')
    selected_age_rating_id = request.GET.get('age_rating')

    all_tv_shows = TVShowsModel.objects.all()
    
    if selected_genre_id:
        #filter films using foreign key in genre
        all_tv_shows = TVShowsModel.objects.filter(genre_id=selected_genre_id)
    if selected_age_rating_id:
        all_tv_shows = TVShowsModel.objects.filter(age_rating_id=selected_age_rating_id)
    
    context = {
        'tv_shows': all_tv_shows,
        'genres' : GenreModel.objects.all(),
        'age_ratings' : AgeRatingModel.objects.all(),
        'selected_genre': selected_genre_id, 
        'selected_age_rating' : selected_age_rating_id,
        }
    return render(request, 'tv_shows.html', context)

#sign up page:
def sign_up(request):
    return render(request, 'sign_up.html')