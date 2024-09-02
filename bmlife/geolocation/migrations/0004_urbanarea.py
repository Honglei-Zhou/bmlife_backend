# Generated by Django 2.2.1 on 2019-05-21 16:48

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geolocation', '0003_auto_20190521_0528'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrbanArea',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('uace10', models.CharField(max_length=5)),
                ('geoid10', models.CharField(max_length=5)),
                ('name10', models.CharField(max_length=100)),
                ('namelsad10', models.CharField(max_length=100)),
                ('lsad10', models.CharField(max_length=2)),
                ('mtfcc10', models.CharField(max_length=5)),
                ('uatyp10', models.CharField(max_length=1)),
                ('funcstat10', models.CharField(max_length=1)),
                ('aland10', models.FloatField()),
                ('awater10', models.FloatField()),
                ('intptlat10', models.CharField(max_length=11)),
                ('intptlon10', models.CharField(max_length=12)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
    ]