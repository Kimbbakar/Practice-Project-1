# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 14:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0008_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]
