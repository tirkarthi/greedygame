# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_collection', '0002_auto_20160710_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='Genre',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='Rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='Title',
            new_name='title',
        ),
    ]
