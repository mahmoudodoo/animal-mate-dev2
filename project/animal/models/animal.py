from django.db import models
from django.utils.text import slugify
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
import os
from django.dispatch import receiver
from django.db.models.signals import post_delete


ANIMALREQUEST_STATUS = (
    ('1', _('Under Review')),
    ('2', _('Rejected')),
    ('3', _('Accepted')),
 
)

class AnimalRequest(models.Model):
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    status = models.CharField(choices=ANIMALREQUEST_STATUS, max_length=255, default='1')
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Animal request date')
    )

    def __str__(self):
        return self.get_status_display()
    
    def cat_name(self):
        return self.animal.name
    
    def user_cat(self):
        return self.animal.user
    
    def birth_day(self):
        return self.animal.birth_day
    
    def cat_city(self):
        return f'{self.animal.country} - {self.animal.city}'
    
    def cat_price(self):
        return self.animal.price



class Animal(models.Model):
    name = models.CharField(max_length=255)
    birth_day = models.DateField()
    user = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    categ = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_for_animal_currency = models.CharField(max_length=255)
    desc = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    index_page = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Animal, self).save(*args, **kwargs)
        if self.pk:
            # Create a new AnimalRequest associated with the newly created Animal
            AnimalRequest.objects.create(animal=self, status='1')

    def delete(self, *args, **kwargs):
        # Delete associated AnimalImage instances and their image files
        for image in self.animalimage_set.all():
            image.delete()
        
        super(Animal, self).delete(*args, **kwargs)


    def __str__(self):
        return self.name




class AnimalImage(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='animal_images/')

    def __str__(self):
        return f"{self.animal.name} - Image"
    
    def delete(self, *args, **kwargs):
        # Remove the image file from the media directory when the instance is deleted
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        
        super(AnimalImage, self).delete(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Animal Images'


@receiver(post_delete, sender=AnimalImage)
def delete_image_file(sender, instance, **kwargs):
    # Delete the image file from the media directory when an AnimalImage instance is deleted
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

class AnimalPriceForStripe(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
    






