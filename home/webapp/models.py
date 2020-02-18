from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=30)
    phoneno = models.IntegerField()
    category = models.CharField(max_length=30)
    baseprice = models.IntegerField()
    bidprice = models.IntegerField()
    city = models.CharField(max_length=30)
