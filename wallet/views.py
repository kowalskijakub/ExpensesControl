from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AddExpense

# Create your views here.
@login_required
def wallet(request):
    return render(request, 'wallet/myWallet.html', {})

@login_required
def addToWallet(request):
    form = AddExpense
    return render(request, 'wallet/addToWallet.html', {'form': form})