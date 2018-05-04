from django.db import models
from django.contrib.auth.models import User
from .utils import predict_model
from django.db.models.signals import pre_save, post_save

# Create your models here
class Company(models.Model):
    facebook_name = models.CharField(max_length=20)
    amount        = models.IntegerField()
    duration      = models.IntegerField()
    result        = models.IntegerField(default='')

# -------------This code generates slugs automatically--------

def rl_pre_save_receiver(sender, instance, *args, **kwargs):      
    if not instance.result:
        instance.result = predict_model(instance)
pre_save.connect(rl_pre_save_receiver, sender=Company)

