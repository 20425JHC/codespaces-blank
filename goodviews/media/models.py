from django.db import models

#For the data tables:
#genre table
class genre(models.Model):
   id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
   genre = models.CharField(max_length=50)

   def __str__(self):
       return f"{self.genre}"

#age_rating table
class age_rating(models.Model):
   id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
   age_rating = models.CharField(max_length=50)

   def __str__(self):
          return f"{self.age_rating}"

#films table
class films(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    films = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    poster = models.URLField(max_length=300)
    trailer = models.URLField(max_length=300)
    year_of_release = models.PositiveSmallIntegerField(null=True, blank=True) 
    runtime = models.CharField(max_length=100)
    age_rating = models.ForeignKey(age_rating, on_delete=models.CASCADE, null=True, blank=True)
    genre = models.ForeignKey(genre, on_delete=models.CASCADE, null=True, blank=True)
    director = models.CharField(max_length = 100, default='Unknown')
    actors = models.CharField(max_length=600)

    def __str__(self):
           return f"{self.films}"

#tv shows table
class tv_shows(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    tv_shows = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    poster = models.URLField(max_length=300)
    trailer = models.URLField(max_length=300)
    year_of_release = models.PositiveSmallIntegerField(null=True, blank=True)
    number_of_seasons = models.CharField(max_length=3, null=True)
    age_rating = models.ForeignKey(age_rating, on_delete=models.CASCADE, null=True, blank=True)
    genre = models.ForeignKey(genre, on_delete=models.CASCADE, null=True, blank=True)
    director = models.CharField(max_length=100, default='Unknown')
    actors = models.CharField(max_length=600)

    def __str__(self):
           return f"{self.tv_shows}"