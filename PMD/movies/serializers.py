# -*- coding: utf-8 -*-
from .models import Genre, Movie, Season, Episode, UserMovie
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'
        depth = 1


class UserMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMovie
        exclude = ['user']
        depth = 2
