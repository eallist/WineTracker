# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buywine', '0001_squashed_0004_auto_20180918_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='VineyardLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('vineyard_location_desc', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buywine.Country')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buywine.Province')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buywine.State')),
            ],
            options={
                'ordering': ['city', 'state', 'province', 'country'],
                'db_table': 'wt_vineyard_location',
            },
        ),
        migrations.CreateModel(
            name='WineryAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.TextField(blank=True, null=True)),
                ('address_line_2', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=40, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buywine.Country')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buywine.Province')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buywine.State')),
            ],
            options={
                'db_table': 'wt_winery_address',
                'verbose_name_plural': 'Winery Addresses',
            },
        ),
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
        migrations.RemoveField(
            model_name='address',
            name='province',
        ),
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.AlterField(
            model_name='vineyard',
            name='vineyard_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buywine.VineyardLocation'),
        ),
        migrations.AlterField(
            model_name='winery',
            name='winery_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buywine.WineryAddress'),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AlterUniqueTogether(
            name='wineryaddress',
            unique_together=set([('address_line_1', 'address_line_2', 'city', 'state', 'province', 'country', 'zip_code')]),
        ),
        migrations.AlterUniqueTogether(
            name='vineyardlocation',
            unique_together=set([('city', 'state', 'province', 'country', 'vineyard_location_desc')]),
        ),
    ]