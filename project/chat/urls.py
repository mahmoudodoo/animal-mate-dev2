# urls.py
from django.urls import path
from . import apis, views

urlpatterns = [
    path('api/messages/', apis.MessageListCreateView.as_view(), name='message-list-create'),
    path('chat_room/<slug:slug>', views.chat_room, name='chat_room'),
    path('chat_rooms/', views.chat_rooms, name='chat_rooms'),
]
