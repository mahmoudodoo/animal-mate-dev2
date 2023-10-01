from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def profile_account_url(request):
    return render(request, 'profile_account_url.html')