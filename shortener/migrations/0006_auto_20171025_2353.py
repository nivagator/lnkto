# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-26 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20171024_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lnktourl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_dot_com, shortener.validators.validate_url]),
        ),
    ]