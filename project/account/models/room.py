from django.db import models
from django.utils.text import slugify
from .user import Account 

class Room(models.Model):
    name = models.CharField(max_length=255)
    user_1 = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_1_rooms')
    user_2 = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_2_rooms')
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    connect_id = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
