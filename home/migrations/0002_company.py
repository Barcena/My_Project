# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-02 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
