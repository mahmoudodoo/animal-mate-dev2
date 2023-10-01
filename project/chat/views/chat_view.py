from django.shortcuts import render
from account.models import Room, Account
from django.db.models import Q
from ..models import Message
from django.contrib.auth.decorators import login_required

@login_required
def chat_rooms(request):
    current_user = request.user
    user_rooms = Room.objects.filter(Q(user_1=current_user) | Q(user_2=current_user))
    context = {
        'user_rooms': user_rooms
    }
    return render(request, 'chat_rooms.html', context)

@login_required
def chat_room(request, slug):
    room = Room.objects.get(slug=slug)
    chat_messages = Message.objects.filter(room=room).order_by('timestamp')[0:300]
    return render(request, 'chat_room.html', context={'room': room, 'chat_messages': chat_messages})
