from django.db import models

#table
class genre(models.Model):
   id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
   genre = models.CharField(max_length=50)

class age_rating(models.Model):
   id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
   age_rating = models.CharField(max_length=50)


class films(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    poster = models.URLField(max_length=300)
    trailer = models.URLField(max_length=300)
    year_of_release = models.PositiveSmallIntegerField 
    runtime = models.CharField(max_length=100)
    age_ratingID = models.PositiveSmallIntegerField
    genreID = models.PositiveSmallIntegerField
    director = models.CharField(max_length = 100, default='Unknown')
    actors = models.CharField(max_length=600)

class tv_shows(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    poster = models.URLField(max_length=300)
    trailer = models.URLField(max_length=300)
    year_of_release = models.PositiveSmallIntegerField
    number_of_seasons = models.PositiveSmallIntegerField
    age_ratingID = models.PositiveSmallIntegerField
    genreID = models.PositiveSmallIntegerField
    director = models.CharField(max_length=100, default='Unknown')
    actors = models.CharField(max_length=600)