from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Piece(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title