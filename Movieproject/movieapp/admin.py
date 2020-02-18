from django.contrib import admin
from movieapp.models import Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ['moviename', 'rdate', 'hero', 'heroin', 'rating']


admin.site.register(Movie, MovieAdmin)