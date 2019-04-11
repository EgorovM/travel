# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-09 09:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190409_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrepreneur',
            name='photo',
            field=models.ImageField(default='images/home_default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='entrepreneur',
            name='status',
            field=models.CharField(choices=[('repair', 'Ремонт'), ('home', 'Жилье')], max_length=50),
        ),
        migrations.AlterField(
            model_name='point',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 4, 9, 9, 54, 8, 987665, tzinfo=utc)),
        ),
    ]