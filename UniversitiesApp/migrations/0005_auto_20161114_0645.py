# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UniversitiesApp', '0004_auto_20161108_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='photo',
            field=models.ImageField(default=0, upload_to='static/universityimages'),
        ),
        migrations.AlterField(
            model_name='university',
            name='website',
            field=models.CharField(default='/', max_length=300),
        ),
    ]