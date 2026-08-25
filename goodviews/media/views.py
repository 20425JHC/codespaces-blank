from django.shortcuts import render
'''importing the models/tables from models.py to retrieve the information of each row and it's own special requirements'''
from .models import films as FilmsModel, tv_shows as TVShowsModel, genre as GenreModel, age_rating as AgeRatingModel

'''views function helps tell the pregramme what parts of the database from what models to display in the website and specify any requirements. It later tells the programme where to link and display the information just received.
Example: in home page the function tells programme to get data from specific columns and rows and to show films and shows only if the year released is greater than or equal to 2020, 
and then tells programme to render the request and display the content in home.html '''

#home page
def home(request):
    selected_year_of_release = request.GET.get('year_of_release')
    selected_genre_id = request.GET.get('genre')
    selected_age_rating_id = request.GET.get('age_rating')

    all_films = FilmsModel.objects.filter(year_of_release__gte='2020').values()
    all_tv_shows = TVShowsModel.objects.filter(year_of_release__gte='2020').values()
    
    context = {
        'films': all_films,
        'tv_shows' : all_tv_shows,
        'genres': GenreModel.objects.all(),
        'age_ratings': AgeRatingModel.objects.all(),
        'selected_year_of_release' : selected_year_of_release,
        'selected_genre': selected_genre_id,
        'selected_age_rating': selected_age_rating_id, 
        }
    return render(request, 'home.html', context)

#Contact Page
def contact_us(request):
    return render(request, 'contact_us.html')

#films page
def films(request):
    selected_genre_id = request.GET.get('genre')
    selected_age_rating_id = request.GET.get('age_rating')

    # Build a dictionary for active filters
    '''This is a specific requirement as there are two filters working together, creating a dictionary combines them and doesn't let them cancel each other'''
    filter_kwargs = {}

    if selected_genre_id and selected_genre_id != '':
        filter_kwargs['genre_id'] = selected_genre_id

    if selected_age_rating_id and selected_age_rating_id != '':
        filter_kwargs['age_rating_id'] = selected_age_rating_id

    # Unpack the dictionary into filter() using **
    # If both IDs are present, this becomes: .filter(genre_id=X, age_rating_id=Y)
    # If no IDs are present, filter(**{}) simply returns all films.
    all_films = FilmsModel.objects.filter(**filter_kwargs)

    context = {
        'films': all_films,
        'genres': GenreModel.objects.all(),
        'age_ratings': AgeRatingModel.objects.all(),
        'selected_genre': selected_genre_id,
        'selected_age_rating': selected_age_rating_id, 
    }
    return render(request, 'films.html', context)

#tv shows page
def tv_shows(request):
    selected_genre_id = request.GET.get('genre')
    selected_age_rating_id = request.GET.get('age_rating')

    # Build a dictionary for active filters
    '''This is a specific requirement as there are two filters working together, creating a dictionary combines them and doesn't let them cancel each other'''
    filter_kwargs = {}

    if selected_genre_id:
        filter_kwargs['genre_id'] = selected_genre_id
        
    if selected_age_rating_id:
        filter_kwargs['age_rating_id'] = selected_age_rating_id

    # Unpack the dictionary into filter() using **
    # If both IDs are present, this becomes: .filter(genre_id=X, age_rating_id=Y)
    # If no IDs are present, filter(**{}) simply returns all films.
    all_tv_shows = TVShowsModel.objects.filter(**filter_kwargs)
    
    context = {
        'tv_shows': all_tv_shows,
        'genres' : GenreModel.objects.all(),
        'age_ratings' : AgeRatingModel.objects.all(),
        'selected_genre': selected_genre_id, 
        'selected_age_rating' : selected_age_rating_id,
        }
    return render(request, 'tv_shows.html', context)
