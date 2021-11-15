from django.urls import path
from .views import wallet, addExpense, addIncome

urlpatterns = [
    path('', wallet, name='wallet'),
    path('add_expense/', addExpense, name="addExpense"),
    path('add_income/', addIncome, name="addIncome")
]