# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='air_date',
            field=models.DateField(verbose_name='Date when episode was aired', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(verbose_name='Date when that move was first displayed in cinemas', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(verbose_name='Year that movie was produced', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='year',
            field=models.PositiveSmallIntegerField(verbose_name='Year when season was produced', blank=True, null=True),
        ),
    ]
