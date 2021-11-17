from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import formExpense, formIncome
from django.contrib import messages
from .models import PAYMENT_METHOD, Expense, Income
from datetime import date, datetime
from django.db.models import Sum

# Create your views here.
@login_required
def wallet(request):
    expenses = Expense.objects.filter(userID=request.user).order_by('-date')[:5]
    incomes = Income.objects.filter(userID=request.user).order_by('-date')[:5]
    
    thisMonth = datetime.now().strftime('%Y-%m')
    sumExpense = Expense.objects.filter(date__icontains = thisMonth, userID = request.user).aggregate(sumAmount=Sum('amount'))['sumAmount']
    if sumExpense == None:
        sumExpense= 0
    sumIncome = Income.objects.filter(date__icontains = thisMonth, userID = request.user).aggregate(sumAmount=Sum('amount'))['sumAmount']
    if sumIncome == None:
        sumIncome= 0
    total = sumIncome - sumExpense
    print(sumIncome)
    context = {
        'expenses': expenses,
        'incomes': incomes,
        'sumExpense': sumExpense,
        'sumIncome': sumIncome,
        'total': total
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

    thisMonth = datetime.now().strftime('%Y-%m')
    sumExpense = Expense.objects.filter(date__icontains = thisMonth, userID = request.user).aggregate(sumAmount=Sum('amount'))['sumAmount']
    if sumExpense == None:
        sumExpense= 0
    sumCash = Expense.objects.filter(date__icontains = thisMonth, userID = request.user, paymentMethod='C').aggregate(sumAmount=Sum('amount'))['sumAmount']
    if sumCash == None:
        sumCash= 0
    sumBank = Expense.objects.filter(date__icontains = thisMonth, userID = request.user, paymentMethod='B').aggregate(sumAmount=Sum('amount'))['sumAmount']
    if sumBank== None:
        sumBank= 0

    context ={
        'sumExpense': sumExpense,
        'expenses': expenses,
        'sumCash': sumCash,
        'sumBank': sumBank
    }
    return render(request, 'wallet/expenses.html', context)

@login_required
def incomesList(request):
    incomes = Income.objects.filter(userID=request.user).order_by('-date')

    thisMonth = datetime.now().strftime('%Y-%m')
    sumIncome = Income.objects.filter(date__icontains = thisMonth, userID = request.user).aggregate(sumAmount=Sum('amount'))['sumAmount']
    if sumIncome == None:
        sumIncome= 0
    sumCash = Income.objects.filter(date__icontains = thisMonth, userID = request.user, paymentMethod='C').aggregate(sumAmount=Sum('amount'))['sumAmount']
    if sumCash == None:
        sumCash= 0
    sumBank = Income.objects.filter(date__icontains = thisMonth, userID = request.user, paymentMethod='B').aggregate(sumAmount=Sum('amount'))['sumAmount']
    if sumBank== None:
        sumBank= 0

    context ={
        'sumIncome': sumIncome,
        'incomes': incomes,
        'sumCash': sumCash,
        'sumBank': sumBank
    }
    return render(request, 'wallet/incomes.html', context)

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

@login_required
def deleteExpense(request, idProduct):
    Expense.objects.filter(id=idProduct).delete()
    return redirect('expensesList')

@login_required
def deleteIncome(request, idProduct):
    Income.objects.filter(id=idProduct).delete()
    return redirect('incomesList')