from test_plus.test import TestCase

from ..models import Movie, Genre
from random import randint, choice
import datetime


class TestMovieDataModel(TestCase):
    def setUp(self):
        DataProvider.rand_genre()
        DataProvider.rand_movie()
        DataProvider.assign_movie_genre()

    def test_show_genre(self):
        a = Genre.objects.all()
        self.assertTrue(len(a) == 10, 'Genres should have 10 objects')

    def test_show_movie(self):
        a = Movie.objects.all()
        self.assertTrue((len(a)) == 30, 'Movies should have 10 objects')

    def test_query(self):
        genre = Genre.objects.filter(name='Genre 1')
        filtered = Movie.objects.filter(genre=genre)
        print(filtered)


class DataProvider:
    @staticmethod
    def rand_movie():
        for i in range(30):
            obj = Movie(title='Test title {}'.format(i), year=2000, release_date=DataProvider.random_date(),
                        is_series=False)
            obj.save()

    @staticmethod
    def rand_genre():
        for i in range(10):
            obj = Genre(name='Genre {}'.format(i))
            obj.save()

    @staticmethod
    def assign_movie_genre():
        movies = Movie.objects.all()
        genres = Genre.objects.all()
        for movie in movies:
            genre = choice(genres)
            movie.genre.add(genre)
            movie.save()

    @staticmethod
    def random_date():
        date = datetime.date(randint(1000, 2015), randint(1, 12), randint(1, 28))
        return '{:%Y-%m-%d}'.format(date)
