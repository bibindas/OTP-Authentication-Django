# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='ID')),
                ('name', models.CharField(max_length=35, db_column='Name')),
                ('district', models.CharField(max_length=20, db_column='District')),
                ('population', models.IntegerField(db_column='Population')),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True, db_column='Code')),
                ('name', models.CharField(max_length=52, db_column='Name')),
                ('continent', models.CharField(max_length=13, db_column='Continent')),
                ('region', models.CharField(max_length=26, db_column='Region')),
                ('surfacearea', models.FloatField(db_column='SurfaceArea')),
                ('indepyear', models.SmallIntegerField(null=True, db_column='IndepYear', blank=True)),
                ('population', models.IntegerField(db_column='Population')),
                ('lifeexpectancy', models.FloatField(null=True, db_column='LifeExpectancy', blank=True)),
                ('gnp', models.FloatField(null=True, db_column='GNP', blank=True)),
                ('gnpold', models.FloatField(null=True, db_column='GNPOld', blank=True)),
                ('localname', models.CharField(max_length=45, db_column='LocalName')),
                ('governmentform', models.CharField(max_length=45, db_column='GovernmentForm')),
                ('headofstate', models.CharField(max_length=60, null=True, db_column='HeadOfState', blank=True)),
                ('capital', models.IntegerField(null=True, db_column='Capital', blank=True)),
                ('code2', models.CharField(max_length=2, db_column='Code2')),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='countrycode',
            field=models.ForeignKey(to='task.Country', db_column='CountryCode'),
        ),
    ]
