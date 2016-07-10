# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_collection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='Genre',
        ),
        migrations.AddField(
            model_name='track',
            name='Genre',
            field=models.ManyToManyField(to='music_collection.Genre'),
        ),
    ]
