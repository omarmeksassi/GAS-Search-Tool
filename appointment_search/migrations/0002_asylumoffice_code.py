# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asylumoffice',
            name='code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
