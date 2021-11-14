from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddExpense
from django.contrib import messages
from .models import Expense

# Create your views here.
@login_required
def wallet(request):
    return render(request, 'wallet/myWallet.html', {})

@login_required
def addToWallet(request):
    if request.method == 'POST':
        post = request.POST
        form = AddExpense(post)
        
        if form.is_valid():
            Expense.objects.create(userID = request.user, amount = post['amount'], 
                                    date = post['date'], source = post['source'], 
                                    paymentMethod = post['paymentMethod'])
            username = request.user.username
            messages.success(request, f'Expense added for {username}')
        else:
            form = AddExpense
    else:
        form = AddExpense
    return render(request, 'wallet/addToWallet.html', {'form': form})