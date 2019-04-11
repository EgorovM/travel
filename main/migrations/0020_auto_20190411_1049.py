# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-11 01:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20190411_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='rate_name',
            field=models.CharField(default='Новенький', max_length=50),
        ),
        migrations.AlterField(
            model_name='point',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 4, 11, 1, 49, 35, 150337, tzinfo=utc)),
        ),
    ]
