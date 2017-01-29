# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 03:46
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import home.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_agendaindexpage_agendapage'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendapage',
            name='mapa',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock()), ('alignment', home.models.ImageFormatChoiceBlock())), icon='image', label='Aligned image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('one_column', wagtail.wagtailcore.blocks.StructBlock((('back_image', wagtail.wagtailimages.blocks.ImageChooserBlock(blank=True)), ('background_size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('auto', 'Auto'), ('cover', 'Cover'), ('50%', 'Small'), ('200%', 'Large')], default='auto')), ('background_x_position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')], default='50%')), ('background_y_position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')], default='50%')), ('text_align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Centre')], default='center')), ('one_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock())), icon='arrow-left', label='Parallax content'))))), ('two_columns', wagtail.wagtailcore.blocks.StructBlock((('background', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('white', 'White'), ('black', 'Black')], default='white')), ('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True)))))), icon='arrow-left', label='Left column content')), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True)))))), icon='arrow-right', label='Right column content'))))), ('three_columns', wagtail.wagtailcore.blocks.StructBlock((('background', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('white', 'White'), ('black', 'Black')], default='white')), ('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True)))))), icon='arrow-left', label='Left column content')), ('center_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True)))))), icon='arrow-right', label='Center column content')), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True)))))), icon='arrow-right', label='Right column content'))))), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_long', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_lat', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True))))))),
            preserve_default=False,
        ),
    ]
