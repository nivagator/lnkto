# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-24 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_lnktourl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lnktourl',
            name='shortcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
