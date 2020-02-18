from django.db import models

# Create your models here.
class Company(models.Model):
    cname = models.CharField(max_length=50)
    cemail = models.CharField(max_length=50)
    caddrs = models.CharField(max_length=50)
    cphone= models.CharField(max_length=50)
    cincome = models.FloatField()
    def __str__(self):
        return self.cname
