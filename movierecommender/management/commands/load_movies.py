import csv
import pandas as pd
from django.core.management import BaseCommand
from ...models import Movie

class Command(BaseCommand):
    help = 'Load a movie csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        # Remove any existing data
        print("Clean old movie data")
        Movie.objects.all().delete()
        path = kwargs['path']
        # Read the movie csv file as a dataframe
        movie_df = pd.read_csv(path)
        # Iterate each row in the dataframe
        for index, row in movie_df.iterrows():
            imdb_id = row["imdb_id"]
            genres = row["genres"]
            release_date = row["release_date"]
            original_language = row["original_language"]
            original_title = row["original_title"]
            overview = row["overview"]
            vote_average = row["vote_average"]
            vote_count = row["vote_count"]
            poster_path = row["poster_path"]
            # Populate Movie object for each row
            movie = Movie(imdb_id=imdb_id,
                            genres=genres,
                            original_title=original_title,
                            original_language=original_language,
                            release_date=release_date,
                            overview=overview,
                            vote_average=vote_average,
                            vote_count=vote_count,
                            poster_path=poster_path)
            # Save movie object
            movie.save()
            print(f"Movie: {imdb_id}, {original_title} saved...")

# python manage.py load_movies --path movies.csv