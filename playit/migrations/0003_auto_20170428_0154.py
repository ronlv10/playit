# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playit', '0002_auto_20170428_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_round_score',
            field=models.IntegerField(default=0),
        ),
    ]
