from test_plus.test import TestCase

from PMD.movies.models import Movies, MovieGenres, Genres, Seasons, Episodes
from random import randrange
import datetime


class TestMovieDataModel(TestCase):
    def setUp(self):
        DataProvider.rand_genre()
        DataProvider.rand_movie()
        DataProvider.assign_movie_genres()

    def test_show_genres(self):
        a = Genres.objects.all()
        self.assertTrue(len(a) == 10, 'Genres should have 10 objects')

    def test_show_movies(self):
        a = Movies.objects.all()
        self.assertTrue((len(a)) == 30, 'Movies should have 10 objects')

    def test_query(self):
        genre_id = Genres.objects.filter(name='Genre 1')
        filtered = Movies.objects.filter(moviegenres__genre_id__in=genre_id)
        print(filtered)


class DataProvider:
    @staticmethod
    def rand_movie():
        for i in range(30):
            obj = Movies(title='Test title {}'.format(i), year=2000, release_date=DataProvider.random_date(),
                         is_series=False)
            obj.save()

    @staticmethod
    def rand_genre():
        for i in range(10):
            obj = Genres(name='Genre {}'.format(i))
            obj.save()

    @staticmethod
    def assign_movie_genres():
        for i in range(30):
            obj = MovieGenres(movie_id=Movies(id=i), genre_id=Genres(id=randrange(1, 10)))
            obj.save()

    @staticmethod
    def random_date():
        date = datetime.date(randrange(1000, 2015), randrange(1, 12), randrange(1, 28))
        return '{:%Y-%m-%d}'.format(date)
