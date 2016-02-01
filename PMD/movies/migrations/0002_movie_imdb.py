# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='Movie',
            name='imdb',
            field=models.CharField(blank=True, verbose_name='IMDb Id', max_length=9),
        ),
    ]
