from datetime import datetime

from django.shortcuts import render


# Create your views here.

def home(request):
    current_user = "Isaac Chapman"
    return render(request, 'home.html',{'date': datetime.now(),'login' : current_user})