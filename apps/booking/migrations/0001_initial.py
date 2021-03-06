# Generated by Django 2.2.8 on 2019-12-08 04:42

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(db_index=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_from', models.CharField(max_length=50)),
                ('city_to', models.CharField(max_length=50)),
                ('city_from_name', models.CharField(max_length=50)),
                ('city_to_name', models.CharField(max_length=50)),
                ('fly_from', models.CharField(max_length=50)),
                ('fly_to', models.CharField(max_length=50)),
                ('dt_departure', models.DateTimeField()),
                ('dt_return', models.DateTimeField()),
                ('departure_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('return_date', models.DateField()),
                ('return_time', models.TimeField()),
                ('airlines', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trip_id', models.TextField()),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('city_from', models.CharField(max_length=50)),
                ('city_to', models.CharField(max_length=50)),
                ('airport_from', models.CharField(max_length=3)),
                ('airport_to', models.CharField(max_length=3)),
                ('is_return', models.BooleanField(default=False)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('place_from', django.contrib.postgres.fields.jsonb.JSONField()),
                ('place_to', django.contrib.postgres.fields.jsonb.JSONField()),
                ('departure_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('adults', models.IntegerField(default=0)),
                ('children', models.IntegerField(default=0)),
                ('infants', models.IntegerField(default=0)),
                ('seat_type', models.CharField(max_length=10)),
                ('destination_type', models.CharField(choices=[('round', 'Round Trip'), ('oneway', 'Oneway')], max_length=10)),
            ],
        ),
    ]
