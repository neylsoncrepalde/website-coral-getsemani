# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0016_deprecate_rendition_filter_relation'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('home', '0004_localpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('telephone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address_1', models.CharField(blank=True, max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('post_code', models.CharField(blank=True, max_length=10)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]