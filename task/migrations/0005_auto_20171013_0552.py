# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20171013_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
