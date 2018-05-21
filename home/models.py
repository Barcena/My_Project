from django.db import models
from django.contrib.auth.models import User
from .utils import predict_model
from django.db.models.signals import pre_save, post_save
import urllib
import requests
import datetime

# Create your models here
class Company(models.Model):
    facebook_name = models.CharField(max_length=20)
    amount        = models.IntegerField()
    duration      = models.IntegerField()
    result        = models.IntegerField(default='')
    inflation     = models.FloatField()

# -------------This code generates slugs automatically--------

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.result:
        today = datetime.datetime.now()
        start = today - datetime.timedelta(days=3*365)
        inflation_params = {
            'country': 'mexico',
            'start': start.strftime("%d/%m/%Y"),
            'end': today.strftime("%d/%m/%Y"),
            'format': 'true'
        }
        #res = requests.get('https://www.statbureau.org/calculate-inflation-rate-json?', inflation_params)
        #instance.inflation = float(res.text[1:-1])
        instance.inflation = 20.9
        instance.result = predict_model(instance)
pre_save.connect(rl_pre_save_receiver, sender=Company)