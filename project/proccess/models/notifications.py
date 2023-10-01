from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.urls import reverse
from account.models import Account
from datetime import timedelta

class Notification(models.Model):
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    url = models.URLField(verbose_name='Notification URL')
    read = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    expiration_date = models.DateTimeField()

    def get_absolute_url(self):
        # Define the URL to the notification detail view (if needed)
        return reverse('notification_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-date']

@receiver(post_save, sender=Notification)
def delete_expired_notifications(sender, instance, **kwargs):
    # Calculate the date 10 days ago from the current time
    ten_days_ago = timezone.now() - timedelta(days=10)
    
    # Mark expired notifications as done to avoid deleting them again
    expired_notifications = sender.objects.filter(
        expiration_date__lt=ten_days_ago,
        done=False
    )
    expired_notifications.update(done=True)
    
    # Delete expired notifications
    expired_notifications.delete()
