# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from home.models import Post, Friend

admin.site.register(Post)
admin.site.register(Friend)

