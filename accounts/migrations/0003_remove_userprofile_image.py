# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 16:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
    ]
