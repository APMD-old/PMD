from PMD.movies.models import UserMovie, Movie, Genre
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Cleans all movies from the DB.'

    def handle(self, *args, **options):
        UserMovie.objects.all().delete()
        Movie.objects.all().delete()
        Genre.objects.all().delete()
