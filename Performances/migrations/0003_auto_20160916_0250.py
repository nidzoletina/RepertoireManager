# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-16 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Performances', '0002_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SongOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderInPerformance', models.IntegerField()),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Performances.Performance')),
                ('songs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Performances.song')),
            ],
        ),
        migrations.AddField(
            model_name='performance',
            name='songs',
            field=models.ManyToManyField(through='Performances.SongOrder', to='Performances.song'),
        ),
    ]