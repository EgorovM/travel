# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-09 09:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='rate',
            field=models.CharField(choices=[('Beginner', 'Новичок'), ('Expirienser', 'Опытный'), ('Old', 'Бывалый')], default='Beginner', max_length=50),
        ),
        migrations.AlterField(
            model_name='entrepreneur',
            name='status',
            field=models.CharField(choices=[('Repair', 'Ремонт'), ('Home', 'Жилье')], max_length=50),
        ),
        migrations.AlterField(
            model_name='point',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 4, 9, 9, 44, 11, 513101, tzinfo=utc)),
        ),
    ]
