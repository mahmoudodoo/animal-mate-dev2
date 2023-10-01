
from django.shortcuts import render, redirect
from animal.models import Animal, AnimalImage
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required
def profile_ads(request):
    user = request.user
    animals = Animal.objects.filter(user=user.id).all()
    ads_animals = []
    for animal in animals:
        animal_images = AnimalImage.objects.filter(animal=animal.id).all()
        images_dict = {
            'id': animal.id,
            'name': animal.name,
            'image_1': None,
            'image_2': None,
            'image_3': None,
            'image_4': None,
        }

        # Check if there are images and assign them if available
        if animal_images:
            if len(animal_images) >= 1:
                images_dict['image_1'] = animal_images[0].image
            if len(animal_images) >= 2:
                images_dict['image_2'] = animal_images[1].image
            if len(animal_images) >= 3:
                images_dict['image_3'] = animal_images[2].image
            if len(animal_images) >= 4:
                images_dict['image_4'] = animal_images[2].image

        ads_animals.append(images_dict)
    context = {
        'ads_animals': ads_animals,
    }
    
    return render(request, 'profile_ads.html',context=context)

@csrf_exempt
def delete_animal(request, animal_id):
    ads_animals = []
    if request.method == 'DELETE':
        # Retrieve the animal by its ID
        animal = Animal.objects.get(id=animal_id)     
        # Delete the Animal itself
        if animal:
            animal.delete()
            messages.success(request, 'Animal deleted successfully')
    user = request.user
    animals = Animal.objects.filter(user=user.id).all()

    for animal in animals:
        animal_images = AnimalImage.objects.filter(animal=animal).all()
        images_dict = {
            'id': animal.id,
            'name': animal.name,
            'image_1': None,
            'image_2': None,
            'image_3': None,
            'image_4': None,
        }

        # Check if there are images and assign them if available
        if animal_images:
            if len(animal_images) >= 1:
                images_dict['image_1'] = animal_images[0].image
            if len(animal_images) >= 2:
                images_dict['image_2'] = animal_images[1].image
            if len(animal_images) >= 3:
                images_dict['image_3'] = animal_images[2].image
            if len(animal_images) >= 4:
                images_dict['image_4'] = animal_images[2].image

        ads_animals.append(images_dict)

    context = {
        'ads_animals': ads_animals,
    }
    return render(request, 'update_ads_data.html', context=context)

