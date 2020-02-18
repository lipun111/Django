from django.db import models

# Create your models here.
class Revision(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    addrs = models.CharField(max_length=30)

    def __str__(self):
        return self.name
