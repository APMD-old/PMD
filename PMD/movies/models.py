# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Movie title', max_length=255)
    year = models.PositiveSmallIntegerField('Year that movie was produced', blank=True)
    release_date = models.DateField('Date when that move was first displayed in cinemas', blank=True)
    is_series = models.BooleanField('Boolean to mark if a movie is a series', default=False)

    objects = models.Manager()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Genres(models.Model):
    name = models.CharField('Name of film genre', max_length=50)

    objects = models.Manager()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class MovieGenres(models.Model):
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genres, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.genre_id


@python_2_unicode_compatible
class Seasons(models.Model):
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField('Year when season was produced', blank=True)
    title = models.CharField('Season title', max_length=255)
    season_number = models.PositiveSmallIntegerField('Season number', null=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Episodes(models.Model):
    season_id = models.ForeignKey(Seasons, on_delete=models.CASCADE)
    title = models.CharField('Episode title', max_length=255)
    air_date = models.DateField('Date when episode was aired', blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class UserMovies(models.Model):
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.User')
    location = models.CharField('Movie location on user`s hard drive', max_length=512)
    seen = models.BooleanField('Boolean to mark if user has seen the movie', default=False)

    objects = models.Manager()

    def __str__(self):
        return self.location
