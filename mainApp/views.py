from django.shortcuts import redirect, render


# Create your views here.

def home(request):
    return render(request, 'mainApp/home.html')



