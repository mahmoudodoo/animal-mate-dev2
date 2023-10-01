from django.db import models
from django_countries.fields import CountryField
from location_field.models.plain import PlainLocationField
from django.urls import reverse

class Clinic(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='clinic_images/')
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    tiktok = models.URLField(blank=True)
    thread = models.URLField(blank=True)
    country = CountryField()
    city = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('clinic_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
