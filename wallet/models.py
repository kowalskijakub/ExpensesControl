from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

PAYMENT_METHOD = (
        ('C', 'Cash'),
        ('B', 'Bank'),
    )

class Expense(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(default=datetime.date.today)
    source = models.CharField(max_length=50)
    paymentMethod = models.CharField(max_length=1, choices=PAYMENT_METHOD)
class Income(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(default=datetime.date.today)
    source = models.CharField(max_length=50)
    paymentMethod = models.CharField(max_length=1, choices=PAYMENT_METHOD)