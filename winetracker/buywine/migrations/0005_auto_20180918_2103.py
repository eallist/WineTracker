# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buywine', '0004_auto_20180918_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='WineryVineyard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vineyard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buywine.Vineyard')),
                ('winery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buywine.Winery')),
            ],
            options={
                'ordering': ['winery', 'vineyard'],
                'db_table': 'wt_map_winery_vineyard',
            },
        ),
        migrations.AlterUniqueTogether(
            name='wineryvineyard',
            unique_together=set([('winery', 'vineyard')]),
        ),
    ]