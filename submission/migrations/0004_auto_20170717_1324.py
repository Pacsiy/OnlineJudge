# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-17 13:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_auto_20170704_1243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'ordering': ('-created_time',)},
        ),
    ]