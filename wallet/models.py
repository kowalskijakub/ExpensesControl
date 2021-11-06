from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Expense(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(default=datetime.date.today)
    source = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class Income(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(default=datetime.date.today)
    source = models.CharField(max_length=50)
    type = models.CharField(max_length=50)