# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpage_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='intro',
            field=models.CharField(max_length=500),
        ),
    ]