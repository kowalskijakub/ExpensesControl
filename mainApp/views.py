from django.shortcuts import redirect, render


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('wallet')
    return render(request, 'mainApp/home.html')



