from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    mobile = models.IntegerField()
    password = models.CharField(max_length=8)


class User(models.Model):
    username123 = models.CharField(max_length=8)
    password123 = models.CharField(max_length=8)
