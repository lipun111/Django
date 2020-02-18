from django.db import models
from django.urls import reverse
# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    grade = models.CharField(max_length=64)
    price = models.FloatField()
    phoneno = models.IntegerField()


    def get_absolute_url(self):
        return reverse('Home')
        # kwargs={'pk':self.pk}
