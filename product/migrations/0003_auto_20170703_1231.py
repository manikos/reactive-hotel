# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20170703_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
