# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sender',
            name='sender_movie',
            field=models.FileField(upload_to=b'movies'),
            preserve_default=True,
        ),
    ]
