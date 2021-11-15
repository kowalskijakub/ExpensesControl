from django.urls import path
from .views import wallet, addExpense, addIncome, expensesList, incomesList

urlpatterns = [
    path('', wallet, name='wallet'),
    path('add_expense/', addExpense, name="addExpense"),
    path('add_income/', addIncome, name="addIncome"),
    path('expenses/', expensesList, name="expensesList"),
    path('incomes/', incomesList, name="incomesList")
]