# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 23:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FoodTrucker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='position',
        ),
    ]
