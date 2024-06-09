from django.db import models

# Create your models here.

class Signin(models.Model):
    name = models.CharField(max_length=256)
    phone = models.PositiveIntegerField(default='')
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)
