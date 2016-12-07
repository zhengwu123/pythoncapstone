# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0003_auto_20161207_0502'),
        ('GroupsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='project',
            field=models.ManyToManyField(default=None, related_name='project_groups', to='ProjectsApp.Project'),
        ),
    ]
