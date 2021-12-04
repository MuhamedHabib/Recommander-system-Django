from django.test import TestCase
from .models import Movie

# Create your tests here.
class MovieTestCase(TestCase):

    def setUp(self):
        pass

    # python manage.py test movierecommender.tests.MovieTestCase
    # ./manage.py test
    def test_movies(self):
        john = Movie.objects.get(original_title="Toy Story")
        print(john)



