# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Movie title', max_length=255)
    year = models.PositiveSmallIntegerField('Year that movie was produced', blank=True)
    release_date = models.DateField('Date when that move was first displayed in cinemas', blank=True)
    is_series = models.BooleanField('Boolean to mark if a movie is a series', default=False)
    imdb = models.CharField('IMDb Id', max_length=9, blank=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Genre(models.Model):
    name = models.CharField('Name of film genre', max_length=50)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class MovieGenre(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.genre_id


@python_2_unicode_compatible
class Season(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField('Year when season was produced', blank=True)
    title = models.CharField('Season title', max_length=255)
    season_number = models.PositiveSmallIntegerField('Season number', null=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Episode(models.Model):
    season_id = models.ForeignKey(Season, on_delete=models.CASCADE)
    title = models.CharField('Episode title', max_length=255)
    air_date = models.DateField('Date when episode was aired', blank=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class UserMovie(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.User')
    location = models.CharField('Movie location on user`s hard drive', max_length=512)
    seen = models.BooleanField('Boolean to mark if user has seen the movie', default=False)

    def __str__(self):
        return self.location
