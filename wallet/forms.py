from django import forms
from django.contrib.auth.models import User
from .models import Expense, Income, PAYMENT_METHOD
import datetime



class formExpense(forms.ModelForm):
    amount = forms.DecimalField(max_digits=6, decimal_places=2)
    date = forms.DateField(initial=datetime.date.today, label='Date [yyyy-mm-dd]')
    source = forms.CharField(max_length=50)
    paymentMethod = forms.ChoiceField(choices=PAYMENT_METHOD, label='Payment Method')
     

    class Meta:
        model = Expense
        fields = ['amount', 'date', 'source', 'paymentMethod']

class formIncome(forms.ModelForm):
    amount = forms.DecimalField(max_digits=6, decimal_places=2)
    date = forms.DateField(initial=datetime.date.today, label='Date [yyyy-mm-dd]')
    source = forms.CharField(max_length=50)
    paymentMethod = forms.ChoiceField(choices=PAYMENT_METHOD, label='Payment Method')
     

    class Meta:
        model = Income
        fields = ['amount', 'date', 'source', 'paymentMethod']

