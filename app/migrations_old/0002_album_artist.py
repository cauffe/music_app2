# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(blank=True, to='app.Artist', null=True),
        ),
    ]
