# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Genre, Movie, Episode, Season, UserMovie

admin.site.register([Genre, Movie, Episode, Season, UserMovie])
