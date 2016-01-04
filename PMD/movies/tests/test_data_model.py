from test_plus.test import TestCase

from PMD.movies.models import Movie, MovieGenre, Genre, Season, Episode
from random import randrange
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
        genre_id = Genre.objects.filter(name='Genre 1')
        filtered = Movie.objects.filter(moviegenre__genre_id__in=genre_id)
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
        for i in range(30):
            obj = MovieGenre(movie_id=Movie(id=i), genre_id=Genre(id=randrange(1, 10)))
            obj.save()

    @staticmethod
    def random_date():
        date = datetime.date(randrange(1000, 2015), randrange(1, 12), randrange(1, 28))
        return '{:%Y-%m-%d}'.format(date)
