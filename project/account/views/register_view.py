from django.contrib.auth import login
from django.shortcuts import render, redirect
from ..forms import SignUpForm

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect URL after registration
    else:
        form = SignUpForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)
