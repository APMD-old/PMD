# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from allauth.socialaccount.views import LoginCancelledView
from braces.views import LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin
from django.views.generic import View, TemplateView
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


# TODO django rest framework zamiast tego
class MovieListView(LoginRequiredMixin, JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        movie_dict = {
            'title': 'Han Solo Dies',
            'poster': 'http://ia.media-imdb.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_SY317_CR0,0,214,317_AL_.jpg'
        }
        return self.render_json_response([movie_dict] * 12)
