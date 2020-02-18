from django.db import models

# Create your models here.

# Abstract base model inheritance

class ContactInfo(models.Model):
    name = models.CharField(max_length = 64)
    email = models.EmailField()
    address = models.CharField(max_length = 120)
    class Meta:
        abstract = True


class Student(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher(ContactInfo):
    subject = models.CharField(max_length = 64)
    salary = models.FloatField()

# Multi table inheritance

class ContactInfo1(models.Model):
    name = models.CharField(max_length = 64)
    email = models.EmailField()
    address = models.CharField(max_length = 120)


class Student1(ContactInfo1):
    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher1(ContactInfo1):
    subject = models.CharField(max_length = 64)
    salary = models.FloatField()
