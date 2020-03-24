# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-24 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200324_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', unique=True),
        ),
    ]
