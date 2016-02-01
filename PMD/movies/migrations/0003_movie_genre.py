# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_imdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviegenre',
            name='genre_id',
        ),
        migrations.RemoveField(
            model_name='moviegenre',
            name='movie_id',
        ),
        migrations.RenameField(
            model_name='episode',
            old_name='season_id',
            new_name='season',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='usermovie',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='usermovie',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='movies.Genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.URLField(verbose_name='The URL of the poster image', default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MovieGenre',
        ),
    ]
