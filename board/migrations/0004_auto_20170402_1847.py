# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-02 18:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20170402_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
