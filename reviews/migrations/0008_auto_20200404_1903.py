# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-04 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20200404_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='after_pic',
            new_name='after_picture',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='before_pic',
            new_name='before_picture',
        ),
    ]
