# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.HomeView.as_view(),
        name='home'
    ),
    url(
        regex=r'^file_upload$',
        view=views.FileUploadView.as_view(),
        name='file_upload'
    ),
    url(
        regex=r'^upload$',
        view=views.FileUploadResponseView.as_view(),
        name='upload'
    ),
    url(
        regex=r'^api/movies/$',
        view=views.MovieListView.as_view(),
        name='movies'
    ),
]
