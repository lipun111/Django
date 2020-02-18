from django.db import models

# Create your models here.


class Movie(models.Model):
    moviename = models.CharField(max_length=30)
    rdate = models.DateField()
    hero = models.CharField(max_length=30)
    heroin = models.CharField(max_length=30)
    rating = models.IntegerField()