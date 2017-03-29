from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from donations.models import donation


# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(User)
    donation = models.ForeignKey(donation)
    quantity = models.IntegerField()
    def __str__(self):
        return "{0} ({1})".format(self.donation.title, self.quantity)
