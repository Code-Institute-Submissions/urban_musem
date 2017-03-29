from __future__ import unicode_literals

from django.db import models

# Create your models here.

class donation(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title