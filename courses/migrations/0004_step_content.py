# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20161205_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
    ]