# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

from braces.views import LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin
from django.views.generic import View, TemplateView
from rest_framework import viewsets

from PMD.externalapi.omdbapi import OmdbApi
from PMD.parser.file_parser import FileParser
from PMD.parser.movie_parser import movies_parser
from .models import UserMovie, Movie, Genre
from .serializers import UserMovieSerializer

log = logging.getLogger(__name__)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'movies/home.html'


class FileUploadView(LoginRequiredMixin, TemplateView):
    template_name = 'movies/file_upload.html'


class FileUploadResponseView(LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin, View):
    def post_ajax(self, request, *args, **kwargs):
        file_text = request.POST['text']

        parser = FileParser()
        directories = parser.read_directories(file_text)
        movies = movies_parser(directories)

        log.info('Parsed {} movies'.format(len(movies)))

        _search_and_create_movies(movies, request.user)

        return self.render_json_response({}, status=200)


class UserMovieViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserMovieSerializer
    queryset = UserMovie.objects.all()

    def get_queryset(self):
        request = self.request
        return UserMovie.objects.filter(user=request.user)


def _search_and_create_movies(movies, user):
    api = OmdbApi()
    for parser_movie in movies:
        if parser_movie.type != 'movie':
            continue

        try:
            api_movie = api.query(precise_title=parser_movie.title, year=parser_movie.year, media=parser_movie.type)
            if api_movie is None:
                raise ValueError('Could not retrieve {} from external API'.format(parser_movie.title))

            genres = api_movie['genre']
            del api_movie['genre']

            movie, created = Movie.objects.get_or_create(**api_movie)
            if created:
                movie.save()

            for genre in genres:
                g, created = Genre.objects.get_or_create(name=genre)
                movie.genre.add(g)
            movie.save()

            try:
                user_movie = UserMovie.objects.get(movie=movie, user=user)
                log.debug('Getting movie {} for user {}'.format(movie, user))
            except UserMovie.DoesNotExist:
                user_movie = UserMovie(movie=movie, user=user)
                log.debug('Creating movie {} for user {}'.format(movie, user))
            user_movie.location = parser_movie.path
            user_movie.save()
        except Exception as e:
            log.warn(e)
