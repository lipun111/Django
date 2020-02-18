from django.db import models

# Create your models here.


class Emp(models.Model):
    name = models.CharField(max_length=30)
    eid = models.IntegerField()
    salary = models.IntegerField()
