from django.contrib import admin

# Register your models here.

from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    fields = ['imdb_id', 'genres', 'original_title', 'overview', 'watched']
    list_display = ('original_title', 'genres', 'release_date', 'watched')
    search_fields = ['original_title', 'overview']


admin.site.register(Movie, MovieAdmin)
