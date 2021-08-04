from django.shortcuts import render
from .models import *

# Create your views here.
def login(request):
    return render(request, 'login.html')

def logining(request, user):
    Username = request.POST['username']
    Password = request.POST['password']
    
    # When input 'username' in html, to compare 'username' and Username.
    account = AuthUser.objects.all(user = Username)
    # To start checking
    if (account.username == Username):
        if (account.password == Password):
            return render(request, '')
    else:
        return render(request, '')