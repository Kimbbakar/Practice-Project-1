# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.6 on 2017-11-30 14:12
=======
# Generated by Django 1.11.6 on 2017-11-30 02:41
>>>>>>> 43bc986ec7a32253a49493d0670ed19aba196a4b
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0007_auto_20171122_0729'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
<<<<<<< HEAD
                ('date', models.DateField(default=datetime.date.today)),
=======
                ('date', models.DateTimeField(default=datetime.date.today)),
>>>>>>> 43bc986ec7a32253a49493d0670ed19aba196a4b
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='classroom.lecture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
