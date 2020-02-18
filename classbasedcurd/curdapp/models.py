from django.db import models
from django.urls import reverse
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30)
    ceo = models.CharField(max_length=30)
    addrs = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.id})
