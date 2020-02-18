from django.db import models
from django.urls import reverse
# Create your models here.

class Emplyoee(models.Model):
    ename = models.CharField(max_length=120)
    eid = models.IntegerField()
    esal = models.FloatField()
    eaddrs = models.CharField(max_length = 120)
    def __str__(self):
        return self.ename

    def get_absolute_url(self):
        return reverse('home')
