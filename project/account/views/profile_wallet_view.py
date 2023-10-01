from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_wallet(request):
    return render(request, 'profile_wallet.html')