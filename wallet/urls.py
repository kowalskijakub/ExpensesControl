from django.urls import path
from .views import wallet, addToWallet

urlpatterns = [
    path('', wallet, name='wallet'),
    path('add/', addToWallet, name="addToWallet")
]