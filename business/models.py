# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


'''class UserProfileManager(models.Manager):
	def  get_queryset(self):
		return super(UserProfileManager, self).get_queryset().filter(city='CDMX')'''

class B2cProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100,default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)
	#image = models.ImageField(upload_to= 'profile_image', blank = True)

	#CDMX=UserProfileManager()

	def __str__(self):
		return self.user.username


def create_b2c_profile(sender,**kwargs):
	if kwargs['created']:
		buisness_profile = B2cProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_b2c_profile, sender=User)


