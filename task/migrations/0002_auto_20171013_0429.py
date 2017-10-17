# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countrylanguage',
            fields=[
                #('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=30, db_column='Language', primary_key=True)),
                ('isofficial', models.CharField(max_length=1, db_column='IsOfficial')),
                ('percentage', models.FloatField(db_column='Percentage')),
                ('countrycode', models.ForeignKey(to='task.Country', db_column='CountryCode')),
            ],
            options={
                'db_table': 'countrylanguage',
            },
        ),
        migrations.AlterUniqueTogether(
            name='countrylanguage',
            unique_together=set([('countrycode', 'language')]),
        ),
    ]
