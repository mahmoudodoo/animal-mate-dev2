from django.db import models
from account.models import Room, Account

class Message(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='messages_sent')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    user_sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='messages_sent_to')
    user_receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='messages_received_from')

    def __str__(self):
        return f'Message from {self.author} in room {self.room}'

    class Meta:
        ordering = ('timestamp',)
