from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    connect_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)
