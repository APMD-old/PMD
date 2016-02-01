import datetime
import random

from django.core.management import BaseCommand

from PMD.movies.models import UserMovie, Genre, Movie
from PMD.users.models import User


def _create_movie(title, poster, genres):
    today = datetime.date.today()
    movie = Movie.objects.create(title=title, poster=poster, year=random.randint(2000, today.year),
                                 release_date=today)
    for genre in genres:
        g, created = Genre.objects.get_or_create(name=genre)
        movie.genre.add(g)
    movie.save()
    return movie


def _create_user_movie(movie, user):
    location = '/media/movies/{}.mp4'.format(movie.title)
    return UserMovie.objects.create(movie=movie, user=user, location=location)


def _create_movies(user):
    movies = []

    movie = _create_movie('Star Wars: The Force Awakens',
                          'http://ia.media-imdb.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1__SX1394_SY684_.jpg',
                          ['Action', 'Adventure', 'Fantasy'])
    movies.append(_create_user_movie(movie, user))

    movie = _create_movie('The Hateful Eight',
                          'http://ia.media-imdb.com/images/M/MV5BMjA1MTc1NTg5NV5BMl5BanBnXkFtZTgwOTM2MDEzNzE@._V1__SX1394_SY684_.jpg',
                          ['Comedy', 'Drama', 'Mystery'])
    movies.append(_create_user_movie(movie, user))

    movie = _create_movie('The Revenant',
                          'http://ia.media-imdb.com/images/M/MV5BMjU4NDExNDM1NF5BMl5BanBnXkFtZTgwMDIyMTgxNzE@._V1__SX1394_SY684_.jpg',
                          ['Adventure', 'Drama', 'Thriller'])
    movies.append(_create_user_movie(movie, user))

    movie = _create_movie('Joy',
                          'http://ia.media-imdb.com/images/M/MV5BMzc2MTI5Mzk0MV5BMl5BanBnXkFtZTgwMDIxMDg1NjE@._V1__SX1394_SY684_.jpg',
                          ['Comedy', 'Drama'])
    movies.append(_create_user_movie(movie, user))

    movie = _create_movie('Deadpool',
                          'http://ia.media-imdb.com/images/M/MV5BMjM3MjEwODA3MF5BMl5BanBnXkFtZTgwNzI4MzM1NzE@._V1__SX1394_SY684_.jpg',
                          ['Action', 'Adventure', 'Sci-Fi'])
    movies.append(_create_user_movie(movie, user))

    movie = _create_movie('The Big Short',
                          'http://ia.media-imdb.com/images/M/MV5BMjM2MTQ2MzcxOF5BMl5BanBnXkFtZTgwNzE4NTUyNzE@._V1__SX1394_SY684_.jpg',
                          ['Biography', 'Drama'])
    movies.append(_create_user_movie(movie, user))

    movie = _create_movie('Daddy\'s Home',
                          'http://ia.media-imdb.com/images/M/MV5BMTQ0OTE1MTk4N15BMl5BanBnXkFtZTgwMDM5OTk5NjE@._V1__SX1394_SY684_.jpg',
                          ['Comedy'])
    movies.append(_create_user_movie(movie, user))

    movie = _create_movie('The Martian',
                          'http://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1__SX1394_SY684_.jpg',
                          ['Adventure', 'Drama', 'Sci-Fi'])
    movies.append(_create_user_movie(movie, user))

    movie = _create_movie('Creed',
                          'http://ia.media-imdb.com/images/M/MV5BODg5NDM1MDI4NF5BMl5BanBnXkFtZTgwMzg0MzQxNzE@._V1__SX1394_SY684_.jpg',
                          ['Drama', 'Sport'])
    movies.append(_create_user_movie(movie, user))

    movie = _create_movie('Sicario',
                          'http://ia.media-imdb.com/images/M/MV5BMjA5NjM3NTk1M15BMl5BanBnXkFtZTgwMzg1MzU2NjE@._V1__SX1394_SY684_.jpg',
                          ['Action', 'Crime', 'Drama'])
    movies.append(_create_user_movie(movie, user))

    movie = _create_movie('Point Break',
                          'http://ia.media-imdb.com/images/M/MV5BMjIxNDkzOTAyNV5BMl5BanBnXkFtZTgwNjEyOTY3NjE@._V1__SX1394_SY684_.jpg',
                          ['Action', 'Crime', 'Sport'])
    movies.append(_create_user_movie(movie, user))

    return len(movies)


class Command(BaseCommand):
    help = 'Create some movies for the specified user. The user must be already created.'

    def add_arguments(self, parser):
        parser.add_argument('user')

    def handle(self, *args, **options):
        username = options['user']
        user = User.objects.get(username=username)

        number = _create_movies(user)
        print('Created {} movies for user {}'.format(number, username))
