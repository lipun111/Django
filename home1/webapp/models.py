from django.db import models

# Create your models here.


class Gpl(models.Model):
    team = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    phoneno = models.IntegerField()
    captain = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)
    golden = models.CharField(max_length=30)