from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import formExpense, formIncome
from django.contrib import messages
from .models import Expense, Income

# Create your views here.
@login_required
def wallet(request):
    expenses = Expense.objects.filter(userID=request.user).order_by('-date')[:5]
    incomes = Income.objects.filter(userID=request.user).order_by('-date')[:5]
    context = {
        'expenses': expenses,
        'incomes': incomes
    }
    return render(request, 'wallet/myWallet.html', context)

@login_required
def addExpense(request):
    if request.method == 'POST':
        post = request.POST
        form = formExpense(post)
        
        if form.is_valid():
            Expense.objects.create(userID = request.user, amount = post['amount'], 
                                    date = post['date'], source = post['source'], 
                                    paymentMethod = post['paymentMethod'])
            username = request.user.username
            messages.success(request, f'Expense added for {username}')
        else:
            form = formExpense
    else:
        form = formExpense
    return render(request, 'wallet/addToWallet.html', {'form': form})

@login_required
def addIncome(request):
    if request.method == 'POST':
        post = request.POST
        form = formIncome(post)
        
        if form.is_valid():
            Income.objects.create(userID = request.user, amount = post['amount'], 
                                    date = post['date'], source = post['source'], 
                                    paymentMethod = post['paymentMethod'])
            username = request.user.username
            messages.success(request, f'Expense added for {username}')
        else:
            form = formIncome
    else:
        form = formIncome
    return render(request, 'wallet/addToWallet.html', {'form': form})

@login_required
def expensesList(request):
    expenses = Expense.objects.filter(userID=request.user).order_by('-date')
    return render(request, 'wallet/expenses.html', {'expenses': expenses})

@login_required
def incomesList(request):
    incomes = Income.objects.filter(userID=request.user).order_by('-date')
    return render(request, 'wallet/incomes.html', {'incomes': incomes})

@login_required
def expenseDetail(request, idProduct):
    
    if request.method == 'POST':
        post = request.POST
        form = formExpense(post)
        Expense.objects.filter(id=idProduct).update(
                                            amount = post['amount'], 
                                            date = post['date'], 
                                            source = post['source'], 
                                            paymentMethod = post['paymentMethod'])
    expense = Expense.objects.get(id=idProduct)
    form = formExpense(initial={
                            'amount':expense.amount, 
                            'date':expense.date, 
                            'source': expense.source, 
                            'paymentMethod':expense.paymentMethod})
    content = {
        'expense': expense, 
        'form': form
    }
    return render(request, 'wallet/expenseDetail.html', content)

@login_required
def incomeDetail(request, idProduct):
    
    if request.method == 'POST':
        post = request.POST
        form = formIncome(post)
        Income.objects.filter(id=idProduct).update(
                                            amount = post['amount'], 
                                            date = post['date'], 
                                            source = post['source'], 
                                            paymentMethod = post['paymentMethod'])
    income = Income.objects.get(id=idProduct)
    form = formIncome(initial={
                            'amount':income.amount, 
                            'date':income.date, 
                            'source': income.source, 
                            'paymentMethod':income.paymentMethod})
    content = {
        'income': income, 
        'form': form
    }
    return render(request, 'wallet/incomeDetail.html', content)