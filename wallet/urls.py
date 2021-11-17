from django.urls import path
from .views import deleteIncome, incomeDetail, wallet, addExpense, addIncome, expensesList, incomesList, expenseDetail, incomeDetail, deleteExpense, deleteIncome

urlpatterns = [
    path('', wallet, name='wallet'),
    path('add_expense/', addExpense, name="addExpense"),
    path('add_income/', addIncome, name="addIncome"),
    path('expenses/', expensesList, name="expensesList"),
    path('expenseDetail/<int:idProduct>', expenseDetail, name="expenseDetail"),
    path('deleteExpense/<int:idProduct>', deleteExpense, name="deleteExpense"),
    path('incomes/', incomesList, name="incomesList"),
    path('incomeDetail/<int:idProduct>', incomeDetail, name="incomeDetail"),
    path('deleteIncomes/<int:idProduct>', deleteIncome, name="deleteIncome")
]