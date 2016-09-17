# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-17 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Performances', '0005_auto_20160916_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='songs',
            field=models.ManyToManyField(through='Performances.SongOrder', to='Repertoire.song'),
        ),
        migrations.AlterField(
            model_name='songorder',
            name='songs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Repertoire.song'),
        ),
        migrations.DeleteModel(
            name='song',
        ),
    ]
