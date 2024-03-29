# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-10 15:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190411_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Administrator')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Location')),
            ],
        ),
        migrations.AlterField(
            model_name='point',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 4, 10, 15, 40, 28, 629251, tzinfo=utc)),
        ),
    ]
