# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-09 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20170830_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='b2cprofile',
            name='apertura',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='b2cprofile',
            name='business_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='b2cprofile',
            name='cierre',
            field=models.CharField(default='', max_length=100),
        ),
    ]
