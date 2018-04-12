# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


'''class UserProfileManager(models.Manager):
	def  get_queryset(self):
		return super(UserProfileManager, self).get_queryset().filter(city='CDMX')'''

class B2cProfile(models.Model):

	b2c_business = models.OneToOneField(User,on_delete=models.CASCADE)
	business_name = models.CharField(max_length=100,default='')
	description = models.CharField(max_length=100, default='')
	direction = models.CharField(max_length=100, default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)
	apertura = models.CharField(max_length=100, default='')
	cierre = models.CharField(max_length=100, default='')
	#image = models.ImageField(upload_to= 'profile_image', blank = True)

	#CDMX=UserProfileManager()

	




