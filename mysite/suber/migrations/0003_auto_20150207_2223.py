# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suber', '0002_auto_20150207_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suber',
            old_name='recipient_city_text',
            new_name='city_text',
        ),
        migrations.RenameField(
            model_name='suber',
            old_name='recipient_city_zip',
            new_name='city_zip',
        ),
        migrations.RenameField(
            model_name='suber',
            old_name='recipient_country_text',
            new_name='country_text',
        ),
        migrations.RenameField(
            model_name='suber',
            old_name='recipient_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='suber',
            old_name='recipient_street_nr',
            new_name='street_nr',
        ),
        migrations.RenameField(
            model_name='suber',
            old_name='recipient_street_text',
            new_name='street_text',
        ),
    ]
