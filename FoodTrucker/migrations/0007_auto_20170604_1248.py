# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodTrucker', '0006_auto_20170604_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='location',
            field=models.IntegerField(verbose_name='Location Name'),
        ),
    ]
