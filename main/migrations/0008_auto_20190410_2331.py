# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-10 14:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190410_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 4, 10, 14, 31, 5, 742836, tzinfo=utc)),
        ),
    ]
