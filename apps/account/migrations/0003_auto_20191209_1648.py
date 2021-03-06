# Generated by Django 2.2.8 on 2019-12-09 16:48

import apps.account.models
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191208_0442'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealWatchGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('airlines', models.CharField(blank=True, max_length=100, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='dealwatch',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companioninvite',
            name='invite_code',
            field=models.CharField(default=apps.account.models.generate_invite_code, max_length=50),
        ),
        migrations.AlterField(
            model_name='dealwatch',
            name='airlines',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='dealwatch',
            name='max_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='dealwatch',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='watches', to='account.DealWatchGroup'),
        ),
    ]
