from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model


def login_view(request):

    if request.user.is_authenticated:
            return redirect('home')
    if request.method == 'POST':
        User = get_user_model()
        email = request.POST['email'].lower()
        user = User.objects.filter(email=email).first()
        password = request.POST['password']
        if user and user.check_password(password):
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def logout_view(request):
    logout(request)
    return redirect('login')
