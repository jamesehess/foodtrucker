# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodTrucker', '0017_auto_20170604_1658'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venuetype',
            options={'ordering': ['name'], 'verbose_name': 'Venue Type'},
        ),
        migrations.AlterField(
            model_name='venuetype',
            name='name',
            field=models.CharField(max_length=40, unique=True, verbose_name='Name'),
        ),
    ]