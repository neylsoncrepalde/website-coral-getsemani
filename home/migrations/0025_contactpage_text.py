# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 12:47
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_agendaindexpage_agendapage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
