# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from allauth.socialaccount.views import LoginCancelledView
from braces.views import LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin
from django.views.generic import View, TemplateView
from rest_framework import viewsets

from .models import UserMovie
from .serializers import UserMovieSerializer
from PMD.parser.file_parser import FileParser
from PMD.parser.movie_parser import movies_parser



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

        # Mario can add movies to data base

        response_dict = {'response': file_text}
        return self.render_json_response(response_dict, status=200)


class UserMovieViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserMovieSerializer
    queryset = UserMovie.objects.all()

    def get_queryset(self):
        request = self.request
        return UserMovie.objects.filter(user=request.user)
