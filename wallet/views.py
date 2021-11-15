from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddExpense, AddIncome
from django.contrib import messages
from .models import Expense, Income

# Create your views here.
@login_required
def wallet(request):
    expenses = Expense.objects.filter(userID=request.user).order_by('-date')
    incomes = Income.objects.filter(userID=request.user).order_by('-date')
    context = {
        'expenses': expenses,
        'incomes': incomes
    }
    return render(request, 'wallet/myWallet.html', context)

@login_required
def addExpense(request):
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

@login_required
def addIncome(request):
    if request.method == 'POST':
        post = request.POST
        form = AddIncome(post)
        
        if form.is_valid():
            Income.objects.create(userID = request.user, amount = post['amount'], 
                                    date = post['date'], source = post['source'], 
                                    paymentMethod = post['paymentMethod'])
            username = request.user.username
            messages.success(request, f'Expense added for {username}')
        else:
            form = AddIncome
    else:
        form = AddIncome
    return render(request, 'wallet/addToWallet.html', {'form': form})