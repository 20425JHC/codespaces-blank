#Import the environment and other related things
import os
import csv
import django 

#Initialise django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'goodviews.settings')
django.setup()

#my code:
#import films, tv_shows, age_rating and genre from csv files
from media.models import age_rating, films, genre, tv_shows

'''Importing data functions for each table. We do this by explaining the file path to get to the needed file, and what data to retreive. Example: "id=row['id']" means in the age_rating csv file retreive data in the id column as id". '''
#age rating:
def import_age_rating(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            age_rating.objects.update_or_create(
                id=row['id'],
                defaults={
                    'age_rating' : row['age_rating']
                }
            )
    print("✓ Age ratings imported!")        


#genre
def import_genre(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            genre.objects.update_or_create(
                id=row['id'],
                defaults={
                    'genre' : row['genre']
                }
            )
    print('✓ Genres imported!')

#films
def import_films(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            films.objects.update_or_create(
                id=row['id'],
                defaults={
                    'films' : row['films'],
                    'description' : row['description'],
                    'poster' : row['poster'],
                    'trailer' : row['trailer'],
                    'year_of_release' : row['year_of_release'],
                    'runtime' : row['runtime'],
                    'age_rating_id' : row['age_ratingID'],
                    'genre_id' : row['genreID'],
                    'director' : row['director'],
                    'actors' : row['actors']
                }
            )
    print("✓ Films imported!")

#tv_shows
def import_tv_shows(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tv_shows.objects.update_or_create(
                id=row['id'],
                defaults={
                    'tv_shows' : row['tv_shows'],
                    'description' : row['description'],
                    'poster' : row['poster'],
                    'trailer' : row['trailer'],
                    'year_of_release' : row['year_of_release'],
                    'number_of_seasons' : row['number_of_seasons'],
                    'age_rating_id' : row['age_ratingID'],
                    'genre_id' : row['genreID'],
                    'director' : row['director'],
                    'actors' : row['actors']
                }
            )
    print("✓ TV shows imported!")


'''execution of the importing data code for each csv file to retrieve the data and run the functions coded above:'''
if __name__ == '__main__':
    import_age_rating('age_rating.csv')
    import_genre('genre.csv')
    import_films('films.csv')
    import_tv_shows('tv_shows.csv')
    print("All data imported successfully!")