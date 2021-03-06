# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_usersession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrylanguage',
            name='countrycode',
            field=models.ForeignKey(db_column='CountryCode', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='task.Country'),
        ),
        migrations.AlterField(
            model_name='countrylanguage',
            name='language',
            field=models.CharField(db_column='Language', max_length=30),
        ),
    ]
