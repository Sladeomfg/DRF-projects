# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-28 12:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20170728_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='Channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Channel'),
        ),
    ]
