# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipient_name', models.CharField(max_length=200)),
                ('recipient_street_text', models.CharField(max_length=200)),
                ('recipient_street_nr', models.CharField(max_length=50)),
                ('recipient_city_text', models.CharField(max_length=200)),
                ('recipient_city_zip', models.CharField(max_length=50)),
                ('recipient_country_text', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender_name', models.CharField(max_length=200)),
                ('sender_memo', models.CharField(max_length=500)),
                ('sender_photo', models.ImageField(upload_to=b'photos')),
                ('sender_movie', models.FileField(upload_to=b'movies')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
