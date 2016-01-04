# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Episode title')),
                ('air_date', models.DateField(verbose_name='Date when episode was aired', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name of film genre')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Movie title')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Year that movie was produced', blank=True)),
                ('release_date',
                 models.DateField(verbose_name='Date when that move was first displayed in cinemas', blank=True)),
                (
                'is_series', models.BooleanField(verbose_name='Boolean to mark if a movie is a series', default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('genre_id', models.ForeignKey(to='movies.Genre')),
                ('movie_id', models.ForeignKey(to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('year', models.PositiveSmallIntegerField(verbose_name='Year when season was produced', blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='Season title')),
                ('season_number', models.PositiveSmallIntegerField(null=True, verbose_name='Season number')),
                ('movie_id', models.ForeignKey(to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='UserMovie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('location', models.CharField(max_length=512, verbose_name='Movie location on user`s hard drive')),
                ('seen', models.BooleanField(verbose_name='Boolean to mark if user has seen the movie', default=False)),
                ('movie_id', models.ForeignKey(to='movies.Movie')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='season_id',
            field=models.ForeignKey(to='movies.Season'),
        ),
    ]
