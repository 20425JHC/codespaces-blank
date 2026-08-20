from django.contrib import admin
#my code:
from .models import genre, age_rating, films, tv_shows

# Registering models here so they are shown on the admin site.
#genre
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "genre",)
admin.site.register(genre, GenreAdmin)

#age rating
class Age_RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "age_rating",)
admin.site.register(age_rating, Age_RatingAdmin)

#films
class FilmsAdmin(admin.ModelAdmin):
    list_display = ("id", "films", "description", "year_of_release", "age_rating", "genre",)
admin.site.register(films, FilmsAdmin)

#tv shows
class TV_ShowsAdmin(admin.ModelAdmin):
    list_display = ("id", "tv_shows", "description", "year_of_release", "number_of_seasons", "age_rating", "genre",)
admin.site.register(tv_shows, TV_ShowsAdmin)
