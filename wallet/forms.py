from django import forms
from django.contrib.auth.models import User
from .models import Expense, Income, PAYMENT_METHOD
import datetime



class AddExpense(forms.ModelForm):
    amount = forms.NumberInput()
    date = forms.DateField(initial=datetime.date.today, label='Date [yyyy-mm-dd]')
    source = forms.CharField(max_length=50)
    paymentMethod = forms.ChoiceField(choices=PAYMENT_METHOD)
     

    class Meta:
        model = Expense
        fields = ['amount', 'date', 'source', 'paymentMethod']
