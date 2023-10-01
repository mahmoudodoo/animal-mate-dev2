from django.contrib.auth.models import AbstractUser
from django.db import models
from animal.models import Animal
from location_field.models.plain import PlainLocationField
from geopy.geocoders import Nominatim
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

class Account(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    mobile_number = PhoneNumberField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True,default='profile_images/avatar.jpg')
    location = PlainLocationField(based_fields=['city'],zoom=7,default='POINT(0.0 0.0)')
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stripe_account = models.CharField(max_length=255, blank=True, null=True)
    country = CountryField(max_length=255)
    activate_whatsapp = models.BooleanField(default=False)
    # Define a ManyToManyField for favorite animals
    favorite_animals = models.ManyToManyField(Animal, blank=True)
    # Define a ManyToManyField for user rooms
    user_rooms = models.ManyToManyField('Room', blank=True)

    def __str__(self):
        return self.username
    
    def get_location_info(self):
        if self.location:
            geolocator = Nominatim(user_agent="mate_project")  # Replace with your app name
            location = geolocator.reverse(self.location)
            address = location.address
            return address