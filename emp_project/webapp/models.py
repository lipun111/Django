from django.db import models

# Create your models here.


class Signup(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField()
    phoneno = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=20)