# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-04 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20200404_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='image2',
            new_name='after_pic',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='image1',
            new_name='before_pic',
        ),
    ]
