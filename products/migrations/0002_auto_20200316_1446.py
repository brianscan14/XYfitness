# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-16 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='XYfitness image', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=' XYfitness Product', max_length=100),
        ),
    ]
