#import films, tv_shows, age_rating and genre from csv files
import csv
from media.models import age_rating
from media.models import films
from media.models import genre
from media.models import tv_shows

#age rating:
def import_age_rating(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            age_rating.objects.create(
                id=row['id'],
                age_rating=row['age_rating']
            )

if __name__ == '__main__':
    csv_file_path = 'goodviews/age_rating.csv'
    import_age_rating(csv_file_path)

#films
def import_films(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            films.objects.create(
                id=row['id'],
                name=row['name'],
                description=row['description'],
                poster=row['poster'],
                trailer=row['trailer'],
                year_of_release=row['year_of_release'],
                runtime=row['runtime'],
                age_ratingID=row['age_ratingID'],
                genreID=row['genreID'],
                director=row['director'],
                actors=row['actors']
            )

if __name__ == '__main__':
    csv_file_path = 'goodviews/films.csv'
    import_films(csv_file_path)


#genre
def import_genre(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            genre.objects.create(
                id=row['id'],
                genre=row['genre']
            )

if __name__ == '__main__':
    csv_file_path = 'goodviews/genre.csv'
    import_genre(csv_file_path)


#tv_shows
def import_tv_shows(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tv_shows.objects.create(
                id=row['id'],
                name=row['name'],
                description=row['description'],
                poster=row['poster'],
                trailer=row['trailer'],
                year_of_release=row['year_of_release'],
                number_of_seasons=row['number_of_seasons'],
                age_ratingID=row['age_ratingID'],
                genreID=row['genreID'],
                director=row['director'],
                actors=row['actors']
            )

if __name__ == '__main__':
    csv_file_path = 'goodviews/tv_shows.csv'
    import_tv_shows(csv_file_path)

