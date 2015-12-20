# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'movies/home.html'


class FileUploadView(LoginRequiredMixin, TemplateView):
    template_name = 'movies/file_upload.html'
