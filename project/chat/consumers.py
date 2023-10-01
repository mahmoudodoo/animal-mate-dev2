import json
from account.models import Account,Room
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message
from django.utils import timezone

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Handle disconnection logic
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        username = data['username']
        room = data['room']
        profile_pic = self.scope['user'].profile_image.url
        timestamp = timezone.now()

        await self.save_message(username, room, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'profile_pic': profile_pic,
                'timestamp': timestamp.strftime('%b. %d, %Y, %I:%M %p'),
            }
        )
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        profile_pic = event['profile_pic']
        timestamp = event['timestamp']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'profile_pic': profile_pic,
            'timestamp': timestamp
        }))


    @sync_to_async
    def save_message(self, username, room_slug, message):
        user_sender = Account.objects.get(username=username)
        room = Room.objects.get(slug=room_slug)

        # Determine the other user in the room
        user_receiver = room.user_1 if user_sender != room.user_1 else room.user_2

        # Save the message with appropriate user_sender and user_receiver
        Message.objects.create(
            author=user_sender,
            room=room,
            content=message,
            user_sender=user_sender,
            user_receiver=user_receiver
        )