# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-06 10:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20200406_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.OneToOneField(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
