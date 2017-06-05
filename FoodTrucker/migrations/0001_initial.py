# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 22:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTruck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('url', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDateTime', models.DateTimeField()),
                ('endDateTime', models.DateTimeField()),
                ('foodtruck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodTrucker.FoodTruck')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodTrucker.Location')),
            ],
        ),
    ]
