from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_home(request):
    order_data = [5, 8, 12, 6, 10, 7, 9, 11, 15, 13]
    return render(request, 'profile_home.html', {'order_data': order_data})

@login_required
def profile_reviews(request):
    return render(request, 'profile_reviews.html')

@login_required
def profile_orders(request):
    return render(request, 'profile_orders.html')

@login_required
def profile_my_settings(request):
    return render(request, 'profile_my_settings.html')

@login_required
def profile_chat_rooms(request):
    return render(request, 'profile_chat_rooms.html')