from django.db import models

# Create your models here.


class Emp(models.Model):
    Eid = models.IntegerField()
    Ename = models.CharField(max_length=40)
    Esal = models.FloatField()
    Eaddr = models.CharField(max_length=40)