# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to=b''),
        ),
    ]
