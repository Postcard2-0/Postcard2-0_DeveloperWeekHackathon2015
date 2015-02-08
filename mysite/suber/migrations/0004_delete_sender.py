# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suber', '0003_auto_20150207_2223'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sender',
        ),
    ]
