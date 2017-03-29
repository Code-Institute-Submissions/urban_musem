from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

# Create your models here.

class Museum (models.Model):
    title = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add= True)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title, self.country, self.city
