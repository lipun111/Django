from django.db import models
from django.urls import reverse
# Create your models here.

class Beer(models.Model):
    name = models.CharField(max_length=64)
    test = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse('home')
        # kwargs={'pk':self.id}
