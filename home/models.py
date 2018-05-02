# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Company(models.Model):
    facebook_name = models.CharField(max_length=20)
    amount = models.IntegerField()
    duration = models.IntegerField()
