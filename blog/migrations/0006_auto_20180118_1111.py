# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-18 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

from ..models import get_image_model_string


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151019_1121'),
    ]

    operations = []

    if get_image_model_string() != 'wagtailimages.Image':
        operations += [
            migrations.AlterField(
                model_name='blogpage',
                name='header_image',
                field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=get_image_model_string(), verbose_name='Header image'),
            ),
        ]
