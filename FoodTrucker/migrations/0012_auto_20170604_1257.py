# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FoodTrucker', '0011_auto_20170604_1256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodtruck',
            options={'ordering': ['name'], 'verbose_name': 'Food Truck'},
        ),
    ]
