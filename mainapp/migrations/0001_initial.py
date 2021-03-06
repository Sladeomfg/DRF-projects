# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-28 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=32)),
                ('Bid', models.FloatField()),
                ('BidTypes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=32)),
                ('Slug', models.CharField(max_length=32)),
                ('BidTypes', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='Channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.channel'),
        ),
    ]
