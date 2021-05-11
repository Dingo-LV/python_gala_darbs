from django.db import models



# Create your models here.

class Deposit(models.Model):
    deposit = models.IntegerField()
    term = models.IntegerField()
    rate = models.DecimalField(decimal_places=2, max_digits=3)
    interest = models.DecimalField(decimal_places=2, max_digits=20)