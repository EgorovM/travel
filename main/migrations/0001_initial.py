# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('about', models.CharField(default='Администрация', max_length=500)),
                ('telephone', models.CharField(default='Не скажу :)', max_length=100)),
                ('photo', models.ImageField(default='images/administrator_default.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(choices=[('Beginner', 'Новичок'), ('Expirienser', 'Опытный'), ('Old', 'Бывалый')], default='Beginner', max_length=50)),
                ('telephone', models.CharField(blank=True, default='Ни скажу!', max_length=100)),
                ('age', models.IntegerField(blank=True, default=18)),
                ('wishes', models.CharField(blank=True, default='Все не почём!', max_length=100)),
                ('photo', models.ImageField(default='images/user_default.jpg', upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Entrepreneur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('repair', 'Ремонт'), ('home', 'Жилье')], max_length=50)),
                ('checked', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('telephone', models.CharField(blank=True, max_length=100)),
                ('addition', models.CharField(blank=True, max_length=500)),
                ('photo', models.ImageField(default='images/home_default.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('repair', models.BooleanField(default=False)),
                ('home', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.datetime(2019, 4, 10, 7, 8, 4, 166734, tzinfo=utc))),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Consumer')),
                ('entrepreneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Entrepreneur')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Consumer')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Location')),
            ],
        ),
        migrations.AddField(
            model_name='filter',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Location'),
        ),
        migrations.AddField(
            model_name='filter',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='entrepreneur',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Location'),
        ),
        migrations.AddField(
            model_name='entrepreneur',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='administrator',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Location'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
