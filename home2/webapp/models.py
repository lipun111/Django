from django.db import models

# Create your models here.


class Gpl(models.Model):
    teamname = models.CharField(max_length=30)
    match = models.IntegerField()
    win = models.IntegerField()
    lose = models.IntegerField()
    draw = models.IntegerField()
    point = models.IntegerField()