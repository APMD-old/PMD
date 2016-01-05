# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from allauth.socialaccount.views import LoginCancelledView
from braces.views import LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin
from django.views.generic import View, TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'movies/home.html'


class FileUploadView(LoginRequiredMixin, TemplateView):
    template_name = 'movies/file_upload.html'


class FileUploadResponseView(LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin, View):
    def post_ajax(self, request, *args, **kwargs):
        file_text = request.POST['text']

        # add file text parser here

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
