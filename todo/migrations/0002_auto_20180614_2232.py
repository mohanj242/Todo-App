# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-14 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='Doing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='Done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='ToDo',
            field=models.BooleanField(default=False),
        ),
    ]
