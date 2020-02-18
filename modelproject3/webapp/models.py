from django.db import models

# Create your models here.


class Emp(models.Model):
    Eid = models.IntegerField()
    Ename = models.CharField(max_length=40)
    Esal = models.IntegerField()
    Eaddr = models.CharField(max_length=40)


class Stu(models.Model):
    Sid = models.IntegerField()
    Sname = models.CharField(max_length=40)
    Ssal = models.IntegerField()
    Saddr = models.CharField(max_length=40)
