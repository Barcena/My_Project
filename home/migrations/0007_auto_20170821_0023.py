# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_friend_current_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.CharField(max_length=500),
        ),
    ]