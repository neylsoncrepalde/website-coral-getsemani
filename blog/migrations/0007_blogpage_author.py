# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170124_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.CharField(default='Neylson Crepalde', max_length=250),
            preserve_default=False,
        ),
    ]