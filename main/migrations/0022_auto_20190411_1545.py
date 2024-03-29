# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-11 06:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20190411_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ar_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('ar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Entrepreneur')),
                ('co', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Consumer')),
            ],
        ),
        migrations.AlterField(
            model_name='point',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 4, 11, 6, 45, 32, 688549, tzinfo=utc)),
        ),
    ]
