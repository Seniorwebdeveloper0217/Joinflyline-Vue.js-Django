# Generated by Django 2.2.8 on 2019-12-11 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0002_auto_20191209_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passport_number',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]