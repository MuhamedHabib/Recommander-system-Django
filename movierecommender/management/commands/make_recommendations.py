from django.core.management import BaseCommand
from ...models import Movie


# Check if genres are valid
def check_valid_genres(genres: str) -> bool:
    if bool(genres and not genres.isspace()) and genres != 'na':
        return True
    else:
        return False

# Add a Jaccard similarity method here

# Add a movie similarity method here


class Command(BaseCommand):
    help = 'Recommend movies'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        # Figure the recommended field for each unwatched movie
        # Based on the similarity on movie genres
        pass


# python manage.py make_recommendations