# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-13 06:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piggybank', '0003_remove_passbook_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passbook',
            name='published_date',
        ),
    ]
